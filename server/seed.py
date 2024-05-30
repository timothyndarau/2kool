from models import db, User, Item, Inventory, BorrowingHistory  # Ensure to import your models
from flask import Flask
from werkzeug.security import generate_password_hash
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Example seed data
users_data = [
    {'username': 'teacher1', 'password': 'password1', 'role': 'teacher'},
    {'username': 'student1', 'password': 'password2', 'role': 'student'},
    {'username': 'admin1', 'password': 'password3', 'role': 'admin'}
]

items_data = [
    {'name': 'Item1', 'description': 'Description for Item 1'},
    {'name': 'Item2', 'description': 'Description for Item 2'}
]

inventory_data = [
    {'item_id': 1, 'quantity': 10},
    {'item_id': 2, 'quantity': 5}
]

borrowing_history_data = [
    {'user_id': 1, 'username': 'teacher1', 'item_id': 1, 'item_name': 'Item1', 'item_description': 'Description for Item 1', 'borrowed_quantity': 2, 'borrowed_at': datetime(2024, 5, 1, 12, 0, 0), 'returned': False},
    {'user_id': 2, 'username': 'student1', 'item_id': 2, 'item_name': 'Item2', 'item_description': 'Description for Item 2', 'borrowed_quantity': 1, 'borrowed_at': datetime(2024, 5, 15, 14, 30, 0), 'returned': True}
]

with app.app_context():
    # Drop all tables and create them again
    db.drop_all()
    db.create_all()

    # Seed users
    for user_data in users_data:
        user_data['password'] = generate_password_hash(user_data['password'], method='pbkdf2:sha256')
        user = User(**user_data)
        db.session.add(user)

    # Seed items
    for item_data in items_data:
        item = Item(name=item_data['name'], description=item_data['description'])
        db.session.add(item)
    
    db.session.commit()  # Commit here to get item IDs
    
    # Seed inventory
    for inv_data in inventory_data:
        inventory = Inventory(**inv_data)
        db.session.add(inventory)

    # Seed borrowing history
    for history_data in borrowing_history_data:
        history = BorrowingHistory(**history_data)
        db.session.add(history)

    db.session.commit()
