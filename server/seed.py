import json
from main import db, app
from models import User, Item, Inventory, BorrowingHistory

# JSON data
seed_data = {
    "users": [
        {
            "username": "admi1",
            "password": "admin_password1",
            "is_admin": True,
            "role": "admin"
        },
        {
            "username": "teacher11",
            "password": "teacher_password1",
            "is_admin": False,
            "role": "teacher"
        },
        {
            "username": "student11",
            "password": "student_password1",
            "is_admin": False,
            "role": "student"
        }
    ],
    "items": [
        {
            "name": "kasuku",
            "description": "A book for writing"
        },
        {
            "name": "stylus",
            "description": "A writing device"
        },
        {
            "name": "tablet",
            "description": "A portable phone"
        }
    ],
    "inventory": [
        {
            "item_id": 1,
            "quantity": 50
        },
        {
            "item_id": 2,
            "quantity": 100
        },
        {
            "item_id": 3,
            "quantity": 20
        }
    ],
    "borrowing_history": [
        {
            "borrower_id": 3,
            "user_id": 2,
            "item_id": 1,
            "returned": False
        },
        {
            "borrower_id": 3,
            "user_id": 2,
            "item_id": 2,
            "returned": False
        }
    ]
}

# Initialize the app context
db.app = app
app.app_context().push()

# Seed users
for user_data in seed_data['users']:
    user = User(**user_data)
    db.session.add(user)

# Commit the changes to the database
db.session.commit()

# Seed items
for item_data in seed_data['items']:
    existing_item = Item.query.filter_by(name=item_data['name']).first()
    if existing_item:
        # Item already exists, update its description
        existing_item.description = item_data['description']
    else:
        # Item does not exist, create a new one
        item = Item(**item_data)
        db.session.add(item)

# Commit the changes to the database
db.session.commit()

# Seed inventory
for inventory_data in seed_data['inventory']:
    inventory = Inventory(**inventory_data)
    db.session.add(inventory)

# Commit the changes to the database
db.session.commit()

# Seed borrowing history
for history_data in seed_data['borrowing_history']:
    history = BorrowingHistory(**history_data)
    db.session.add(history)

# Commit the changes to the database
db.session.commit()

print("Database seeded successfully!")
