from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, Item, BorrowingHistory, User, Inventory  # Import all models

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize extensions
db.init_app(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/login', methods=['POST'])
def login():
    data = request.json  # Assuming the frontend sends JSON data
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()
    if user and user.password == password:
        login_user(user)
        return jsonify({'message': 'Login successful'}), 200
    else:
        return jsonify({'error': 'Invalid username or password'}), 401

@app.route('/signup', methods=['POST'])
def signup():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')

    existing_user = User.query.filter_by(username=username).first()
    existing_email = User.query.filter_by(email=email).first()
    if existing_user:
        return jsonify({'error': 'Username already exists'}), 400
    if existing_email:
        return jsonify({'error': 'Email already exists'}), 400

    new_user = User(username=username, email=email, password=generate_password_hash(password))
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'}), 201

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/admin/dashboard')
@login_required
def admin_dashboard():
    if not current_user.is_admin:
        return redirect(url_for('login'))

    # Example data retrieval for dashboard
    items = Item.query.all()
    return render_template('admin_dashboard.html', items=items)

@app.route('/admin/attempts')
@login_required
def attempted_borrows():
    if not current_user.is_admin:
        return redirect(url_for('login'))

    attempted_borrows = BorrowingHistory.query.all()
    return render_template('attempted_borrows.html', attempted_borrows=attempted_borrows)

@app.route('/input', methods=['POST'])
def add_to_inventory():
    try:
        # Ensure we receive JSON data
        if not request.is_json:
            return jsonify({'error': 'Request must be JSON'}), 400
               
        data = request.json
        item_name = data['itemName']
        quantity = data['quantity']
        description = data.get('description', '')

        # Validate input data
        if not item_name or not quantity:
            return jsonify({'error': 'Item name and quantity are required'}), 400

        # Validate quantity as positive integer
        try:
            quantity = int(quantity)
            if quantity <= 0:
                raise ValueError
        except ValueError:
            return jsonify({'error': 'Quantity must be a positive integer'}), 400

        # Create a new item object
        new_item = Item(name=item_name, description=description)
        db.session.add(new_item)
        db.session.commit()  # Commit to get the item ID

        # Create a new inventory object
        new_inventory = Inventory(item_id=new_item.id, quantity=quantity)
        db.session.add(new_inventory)
        db.session.commit()

        return jsonify({'message': 'Item added successfully'}), 201
    except KeyError as e:
        return jsonify({'error': f'Missing form field: {e}'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
