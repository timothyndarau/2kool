from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(100), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    role = db.Column(db.String(10), nullable=False)  # Role: 'teacher' or 'student'

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Item(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(255))
    quantity = db.Column(db.Integer)
    
    # Update the current_borrows relationship definition
    current_borrows = db.relationship('Borrow', back_populates='item_info', overlaps="item_info")

class Inventory(db.Model):
    __tablename__ = 'inventory'
    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'), nullable=False)  # Change 'items' to 'item'
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.String(255), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)


class BorrowingHistory(db.Model):
    __tablename__ = 'borrowing_history'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    role = db.Column(db.String(10), nullable=False)
    username = db.Column(db.String(150), nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'))
    item_name = db.Column(db.String(150), nullable=False)
    item_description = db.Column(db.Text, nullable=True)
    borrowed_quantity = db.Column(db.Integer, nullable=False)
    returned = db.Column(db.Boolean, default=False)
    borrowed_at = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship('User', backref='borrowing_history')
    item = db.relationship('Item', backref='borrowing_history')

class Borrow(db.Model):
    __tablename__ = 'borrow'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'))
    borrowed_quantity = db.Column(db.Integer)
    borrowed_at = db.Column(db.DateTime)
    returned = db.Column(db.Boolean)
    
    # Define item_info property
    item_info = db.relationship('Item', back_populates='current_borrows')
