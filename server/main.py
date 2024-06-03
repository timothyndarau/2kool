import logging
from flask import Flask, request, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, Item, BorrowingHistory, User, Inventory  # Import all models
from datetime import datetime

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__) 
CORS(app)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db.init_app(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.json  # Assuming the frontend sends JSON data
        username = data.get('username')
        password = data.get('password')

        # Perform login authentication
        user = User.query.filter_by(username=username).first()
        if user and user.check_password( password):
            login_user(user)
            return jsonify({'message': 'Login successful'}), 200
        else:
            return jsonify({'error': 'Invalid username or password'}), 401
    else:
        # If GET request, return a simple message or an HTML template
        return jsonify({'message': 'Please login via POST request with username and password'}), 200

@app.route('/reset-password', methods=['POST'])
def reset_password_request():
    email = request.json.get('email')
    user = User.query.filter_by(email=email).first()
    
    if user:
        # Generate a password reset token (use itsdangerous or similar)
        token = generate_reset_token(user)
        send_reset_email(user.email, token)
    
    return jsonify({'message': 'If your email is in our system, you will receive a password reset link.'}), 200


@app.route('/reset-password/<token>', methods=['POST'])
def reset_password(token):
    new_password = request.json.get('password')
    user = verify_reset_token(token)
    
    if user:
        user.set_password(new_password)
        db.session.commit()
        return jsonify({'message': 'Password has been reset successfully.'}), 200
    
    return jsonify({'message': 'Invalid or expired token.'}), 400


@app.route('/signup', methods=['POST'])
def signup():
    try:
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        role = data.get('role')

        if not username or not password or not role:
            return jsonify({'success': False, 'message': 'Username, password, and role are required'}), 400

        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            return jsonify({'success': False, 'message': 'Username already exists'}), 400

        # Correct the hashing method
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
        new_user = User(username=username, password=hashed_password, role=role)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({'success': True, 'message': 'User created successfully'}), 201
    except Exception as e:
        app.logger.error(f'Error during signup: {str(e)}')
        return jsonify({'success': False, 'message': 'Internal server error'}), 500
    
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return jsonify({'message': 'Logged out successfully'}), 200

@app.route('/borrow', methods=['POST'])
def borrow_item():
    data = request.json
    user_id = data.get('user_id')
    item_id = data.get('item_id')
    quantity = data.get('quantity')

    if not user_id or not item_id or not quantity:
        return jsonify({"error": "Missing user_id, item_id, or quantity"}), 400

    user = User.query.get(user_id)
    item = Item.query.get(item_id)
    inventory = Inventory.query.filter_by(item_id=item_id).first()

    if not user or not item or not inventory:
        return jsonify({"error": "Invalid user_id, item_id, or item not found in inventory"}), 404

    if inventory.quantity < quantity:
        return jsonify({"error": "Not enough items in inventory"}), 400

    # Update inventory
    inventory.quantity -= quantity

    # Add to borrowing history
    history_entry = BorrowingHistory(
        user_id=user.id,
        username=user.username,
        item_id=item.id,
        item_name=item.name,
        item_description=item.description,
        borrowed_quantity=quantity,
        borrowed_at=datetime.utcnow(),
        returned=False
    )
    db.session.add(history_entry)
    db.session.commit()

    return jsonify({"message": "Item borrowed successfully"}), 200

@app.route('/admin/dashboard', methods=['GET'])
@login_required
def admin_dashboard():
    if current_user.role != 'admin':
        return jsonify({'error': 'Access denied'}), 403
    
    items = Item.query.all()
    return jsonify({'items': [item.to_dict() for item in items]}), 200

@app.route('/admin/attempts', methods=['GET'])
@login_required
def attempted_borrows():
    if current_user.role != 'admin':
        return jsonify({'error': 'Access denied'}), 403

    try:
        attempted_borrows = BorrowingHistory.query.all()
        result = []
        for attempt in attempted_borrows:
            item = Item.query.get(attempt.item_id)
            user = User.query.get(attempt.user_id)
            result.append({
                'id': attempt.id,
                'username': user.username if user else 'Unknown',
                'item_name': item.name if item else 'Unknown',
                'borrowed_at': attempt.borrowed_at,
                'returned': attempt.returned
            })
        return jsonify({'attempted_borrows': result}), 200
    except Exception as e:
        app.logger.error(f"Error fetching borrowing history: {str(e)}")
        return jsonify({'error': 'Internal server error'}), 500
    
@app.route('/input', methods=['POST'])
def add_to_inventory():
    try:
        if not request.is_json:
            return jsonify({'error': 'Request must be JSON'}), 400

        data = request.json
        item_name = data['itemName']
        quantity = data['quantity']
        description = data.get('description', '')

        if not item_name or not quantity:
            return jsonify({'error': 'Item name and quantity are required'}), 400

        try:
            quantity = int(quantity)
            if quantity <= 0:
                raise ValueError
        except ValueError:
            return jsonify({'error': 'Quantity must be a positive integer'}), 400

        new_item = Item(name=item_name, description=description)
        db.session.add(new_item)
        db.session.commit()

        new_inventory = Inventory(item_id=new_item.id, quantity=quantity)
        db.session.add(new_inventory)
        db.session.commit()

        return jsonify({'message': 'Item added successfully'}), 201
    except KeyError as e:
        return jsonify({'error': f'Missing form field: {e}'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
