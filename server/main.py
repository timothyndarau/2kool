import logging
from flask import Flask, request, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, Item, BorrowingHistory, User, Inventory  # Import all models

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
        if user and check_password_hash(user.password, password):
            login_user(user)
            return jsonify({'message': 'Login successful'}), 200
        else:
            return jsonify({'error': 'Invalid username or password'}), 401
    else:
        # If GET request, return a simple message or an HTML template
        return jsonify({'message': 'Please login via POST request with username and password'}), 200

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
        return redirect(url_for('login'))
    
    attempted_borrows = BorrowingHistory.query.all()
    return jsonify({'attempted_borrows': [attempt.to_dict() for attempt in attempted_borrows]}), 200

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
