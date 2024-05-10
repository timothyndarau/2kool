from main import db, app
from models import User, Item, Inventory, BorrowingHistory

# Initialize the app context
db.app = app
app.app_context().push()

# Create users
admin = User(username='admin', password='admin_password', is_admin=True, role='admin')
teacher = User(username='teacher1', password='teacher_password', is_admin=False, role='teacher')
student = User(username='student1', password='student_password', is_admin=False, role='student')

# Add users to the session
db.session.add(admin)
db.session.add(teacher)
db.session.add(student)

# Create items
item1 = Item(name='Book', description='A book for reading')
item2 = Item(name='Pen', description='A writing instrument')
item3 = Item(name='Laptop', description='A portable computer')

# Add items to the session
db.session.add(item1)
db.session.add(item2)
db.session.add(item3)

# Commit the changes to the database
db.session.commit()

# Create inventory entries for items
inventory_item1 = Inventory(item_id=item1.id, quantity=50)
inventory_item2 = Inventory(item_id=item2.id, quantity=100)
inventory_item3 = Inventory(item_id=item3.id, quantity=20)

# Add inventory entries to the session
db.session.add(inventory_item1)
db.session.add(inventory_item2)
db.session.add(inventory_item3)

# Commit the changes to the database
db.session.commit()

# Create borrowing history entries
borrowing_history_entry1 = BorrowingHistory(borrower_id=student.id, user_id=teacher.id, item_id=item1.id, returned=False)
borrowing_history_entry2 = BorrowingHistory(borrower_id=student.id, user_id=teacher.id, item_id=item2.id, returned=False)

# Add borrowing history entries to the session
db.session.add(borrowing_history_entry1)
db.session.add(borrowing_history_entry2)

# Commit the changes to the database
db.session.commit()

print("Database seeded successfully!")
