from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, Item, BorrowingHistory, User, Inventory  # Import all models

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db.init_app(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/login', methods=['POST'])
def login():
    # if request.method == 'POST':
        data = request.json  # Assuming the frontend sends JSON data
        username = data.get('username')
        password = data.get('password')

        # Perform login authentication
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            # Login successful
            return jsonify({'message': 'Login successful'}), 200
        else:
            # Login failed
            return jsonify({'error': 'Invalid username or password'}), 401
    # else:
        # Return error for unsupported HTTP method
        # return jsonify({'error': 'Method not allowed'}), 405


@app.route('/signup', methods=['POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        existing_user = User.query.filter_by(username=username).first()
        existing_email = User.query.filter_by(email=email).first()
        if existing_user:
            return jsonify({'error': 'Username already exists'}), 400
        if existing_email:
            return jsonify({'error': 'Email already exists'}), 400
        new_user = User(username=username, email=email)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User created successfully'}), 201
    else:
        return jsonify({'error': 'Method not allowed'}), 405

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
    
    # Example operations:
    # Deleting a specific student by ID
    student = Student.query.get(1)
    db.session.delete(student)
    db.session.commit()
    
    # Fetching a specific teacher by ID and updating their subject
    teacher = Teacher.query.get(1)
    teacher.subject = "Math"
    db.session.commit()
    
    # Querying all teachers
    teachers = Teacher.query.all()

    # Querying all students
    students = Student.query.all()

    # Querying all items
    items = Item.query.all()
    
    return render_template('admin_dashboard.html')

@app.route('/admin/attempts')
@login_required
def attempted_borrows():
    if not current_user.is_admin:
        return redirect(url_for('login'))
    
    # Example operations:
    # Deleting a specific student by ID
    student = Student.query.get(1)
    db.session.delete(student)
    db.session.commit()
    
    # Fetching a specific teacher by ID and updating their subject
    teacher = Teacher.query.get(1)
    teacher.subject = "Math"
    db.session.commit()
    
    # Querying all teachers
    teachers = Teacher.query.all()

    # Querying all students
    students = Student.query.all()

    # Querying all items
    items = Item.query.all()
    
    # Querying all attempted borrows
    attempted_borrows = BorrowingHistory.query.all()
    
    return render_template('attempted_borrows.html', attempted_borrows=attempted_borrows)

@app.route('/input', methods=['POST'])
def add_to_inventory():
    if request.method == 'POST':
        item_name = request.form['itemName']
        quantity = request.form['quantity']
        
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
        new_item = Item(name=item_name, quantity=quantity)
        db.session.add(new_item)
        
        try:
            db.session.commit()
            return jsonify({'message': 'Item added successfully'}), 201
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 500
    else:
        return jsonify({'error': 'Method not allowed'}), 405

if __name__ == '__main__':
    app.run(debug=True)
