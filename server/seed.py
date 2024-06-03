from models import db, User, Item, Inventory, BorrowingHistory
from flask import Flask
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Example seed data
users_data = [
    {'username': 'teacher1', 'password': 'password1', 'role': 'teacher'},
    {'username': 'student1', 'password': 'password2', 'role': 'student'},
    {'username': 'admin1', 'password': 'password3', 'role': 'admin'},
    {'username': 'Rubia Glassup', 'password': '22288', 'role': 'student'},
    {'username': 'Aloise Wanderschek', 'password': '22177', 'role': 'student'},
    {'username': 'Kath Conboy', 'password': '22070', 'role': 'student'},
    {'username': 'Ogden Chagg', 'password': '22229', 'role': 'teacher'},
    {'username': 'Clarice Deniskevich', 'password': '22144', 'role': 'student'},
    {'username': 'Blinnie Ianinotti', 'password': '22280', 'role': 'teacher'},
    {'username': 'Paxon Lalonde', 'password': '22122', 'role': 'teacher'},
    {'username': 'Andrey Martell', 'password': '22288', 'role': 'student'},
    {'username': 'Emmet Girodin', 'password': '22101', 'role': 'student'},
    {'username': 'Carlos Applewhite', 'password': '22183', 'role': 'teacher'},
    {'username': 'Minnie Avrahamian', 'password': '22000', 'role': 'teacher'},
    {'username': 'Tomasina Dwelley', 'password': '22362', 'role': 'student'},
    {'username': 'Henderson Orrah', 'password': '22300', 'role': 'student'},
    {'username': 'Haskel Dregan', 'password': '22425', 'role': 'student'},
    {'username': 'Arlene Gunderson', 'password': '22262', 'role': 'student'},
    {'username': 'Beatrice Boyne', 'password': '22205', 'role': 'student'},
    {'username': 'Rosemary Jupe', 'password': '22419', 'role': 'student'},
    {'username': 'Tierney Cummine', 'password': '22051', 'role': 'teacher'},
    {'username': 'Marcile Tripett', 'password': '22496', 'role': 'student'},
    {'username': 'Charlene Rainon', 'password': '22239', 'role': 'teacher'},
    {'username': 'Zed Straffon', 'password': '22477', 'role': 'student'},
    {'username': 'Hebert Balharry', 'password': '22394', 'role': 'student'},
    {'username': 'Briant Snawden', 'password': '22230', 'role': 'teacher'},
    {'username': 'Roxie Sterley', 'password': '22418', 'role': 'student'},
    {'username': 'Garv Britzius', 'password': '22051', 'role': 'teacher'},
    {'username': 'Callie Bromige', 'password': '22469', 'role': 'teacher'},
    {'username': 'Guillaume Marden', 'password': '22142', 'role': 'teacher'},
    {'username': 'Pebrook Bourdis', 'password': '22071', 'role': 'student'},
    {'username': 'Darryl Stickells', 'password': '22428', 'role': 'student'},
    {'username': 'Anjela Kornilyev', 'password': '22381', 'role': 'student'},
    {'username': 'Teddi Baile', 'password': '22437', 'role': 'student'},
    {'username': 'Janenna Antonowicz', 'password': '22340', 'role': 'student'},
    {'username': 'Issie Deaconson', 'password': '22428', 'role': 'teacher'},
    {'username': 'Julissa Pealing', 'password': '22470', 'role': 'teacher'},
    {'username': 'Quill Jennaroy', 'password': '22101', 'role': 'teacher'},
    {'username': 'Nappie Rodolico', 'password': '22230', 'role': 'teacher'},
    {'username': 'Hussein Josifovic', 'password': '22106', 'role': 'student'},
    {'username': 'Zane Mangeney', 'password': '22355', 'role': 'teacher'},
    {'username': 'Krystyna Brownscombe', 'password': '22184', 'role': 'teacher'},
    {'username': 'Luise Bush', 'password': '22252', 'role': 'student'},
    {'username': 'Bertine Rottery', 'password': '22303', 'role': 'teacher'},
    {'username': 'Grace Eate', 'password': '22386', 'role': 'student'},
    {'username': 'Roanne Wyvill', 'password': '22258', 'role': 'teacher'},
    {'username': 'Hanny Olpin', 'password': '22387', 'role': 'teacher'},
    {'username': 'Mildrid Doding', 'password': '22292', 'role': 'teacher'},
    {'username': 'Chrissie Monson', 'password': '22130', 'role': 'teacher'},
    {'username': 'Sarena Wollard', 'password': '22268', 'role': 'teacher'},
    {'username': 'Lawrence Fellgett', 'password': '22452', 'role': 'student'},
    {'username': 'Brucie Carwithen', 'password': '22195', 'role': 'teacher'},
    {'username': 'Betti MacPaden', 'password': '22418', 'role': 'student'}

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
    {'user_id': 22288, 'role': 'student', 'username': 'Rubia Glassup', 'item_id': 2809, 'item_name': 'notebooks', 'item_description': 'Vintage collectible', 'borrowed_quantity': 3, 'borrowed_at': datetime(2024, 1, 1, 8, 13, 29), 'returned': False},
    {'user_id': 22177, 'role': 'student', 'username': 'Aloise Wanderschek', 'item_id': 3385, 'item_name': 'erasers', 'item_description': 'High-quality item', 'borrowed_quantity': 55, 'borrowed_at': datetime(2024, 1, 3, 15, 23, 25), 'returned': False},
    {'user_id': 22070, 'role': 'student', 'username': 'Kath Conboy', 'item_id': 6942, 'item_name': 'markers', 'item_description': 'Vintage collectible', 'borrowed_quantity': 8, 'borrowed_at': datetime(2024, 1, 3, 11, 44, 26), 'returned': False},
    {'user_id': 22229, 'role': 'teacher', 'username': 'Ogden Chagg', 'item_id': 4169, 'item_name': 'glue sticks', 'item_description': 'High-quality item', 'borrowed_quantity': 11, 'borrowed_at': datetime(2024, 1, 1, 22, 46, 25), 'returned': True},
    {'user_id': 22144, 'role': 'student', 'username': 'Clarice Deniskevich', 'item_id': 9278, 'item_name': 'pencils', 'item_description': 'Vintage collectible', 'borrowed_quantity': 17, 'borrowed_at': datetime(2024, 1, 9, 15, 3, 6), 'returned': False},
    {'user_id': 22280, 'role': 'teacher', 'username': 'Blinnie Ianinotti', 'item_id': 2472, 'item_name': 'rulers', 'item_description': 'High-quality item', 'borrowed_quantity': 48, 'borrowed_at': datetime(2024, 1, 8, 7, 20, 44), 'returned': True},
    {'user_id': 22122, 'role': 'teacher', 'username': 'Paxon Lalonde', 'item_id': 8499, 'item_name': 'calculators', 'item_description': 'Handcrafted masterpiece', 'borrowed_quantity': 40, 'borrowed_at': datetime(2024, 1, 6, 16, 55, 54), 'returned': True},
    {'user_id': 22288, 'role': 'student', 'username': 'Andrey Martell', 'item_id': 5440, 'item_name': 'binders', 'item_description': 'Handcrafted masterpiece', 'borrowed_quantity': 42, 'borrowed_at': datetime(2024, 1, 9, 10, 10, 33), 'returned': False},
    {'user_id': 22101, 'role': 'student', 'username': 'Emmet Girodin', 'item_id': 3732, 'item_name': 'pencils', 'item_description': 'Limited edition piece', 'borrowed_quantity': 57, 'borrowed_at': datetime(2024, 1, 9, 12, 23, 29), 'returned': True},
    {'user_id': 22183, 'role': 'teacher', 'username': 'Carlos Applewhite', 'item_id': 2268, 'item_name': 'markers', 'item_description': 'Limited edition piece', 'borrowed_quantity': 59, 'borrowed_at': datetime(2024, 1, 2, 16, 50, 28), 'returned': False},
    {'user_id': 22000, 'role': 'teacher', 'username': 'Minnie Avrahamian', 'item_id': 5772, 'item_name': 'erasers', 'item_description': 'Vintage collectible', 'borrowed_quantity': 30, 'borrowed_at': datetime(2024, 1, 11, 16, 26, 32), 'returned': False},
    {'user_id': 22362, 'role': 'student', 'username': 'Tomasina Dwelley', 'item_id': 5894, 'item_name': 'folders', 'item_description': 'Handcrafted masterpiece', 'borrowed_quantity': 50, 'borrowed_at': datetime(2024, 1, 9, 15, 2, 38), 'returned': False},
    {'user_id': 22300, 'role': 'student', 'username': 'Henderson Orrah', 'item_id': 6612, 'item_name': 'folders', 'item_description': 'High-quality item', 'borrowed_quantity': 31, 'borrowed_at': datetime(2024, 1, 1, 6, 56, 22), 'returned': True},
    {'user_id': 22425, 'role': 'student', 'username': 'Haskel Dregan', 'item_id': 5029, 'item_name': 'erasers', 'item_description': 'High-quality item', 'borrowed_quantity': 47, 'borrowed_at': datetime(2024, 1, 10, 2, 18, 56), 'returned': False},
    {'user_id': 22262, 'role': 'student', 'username': 'Arlene Gunderson', 'item_id': 1521, 'item_name': 'notebooks', 'item_description': 'Handcrafted masterpiece', 'borrowed_quantity': 17, 'borrowed_at': datetime(2024, 1, 4, 6, 20, 13), 'returned': True},
    {'user_id': 22205, 'role': 'student', 'username': 'Beatrice Boyne', 'item_id': 5210, 'item_name': 'markers', 'item_description': 'Limited edition piece', 'borrowed_quantity': 25, 'borrowed_at': datetime(2024, 1, 9, 4, 55, 21), 'returned': False},
    {'user_id': 22419, 'role': 'student', 'username': 'Rosemary Jupe', 'item_id': 3266, 'item_name': 'folders', 'item_description': 'High-quality item', 'borrowed_quantity': 4, 'borrowed_at': datetime(2024, 1, 5, 1, 35, 16), 'returned': True},
    {'user_id': 22051, 'role': 'teacher', 'username': 'Tierney Cummine', 'item_id': 3005, 'item_name': 'calculators', 'item_description': 'Vintage collectible', 'borrowed_quantity': 24, 'borrowed_at': datetime(2024, 1, 8, 12, 46, 44), 'returned': False},
    {'user_id': 22496, 'role': 'student', 'username': 'Marcile Tripett', 'item_id': 8406, 'item_name': 'glue sticks', 'item_description': 'Handcrafted masterpiece', 'borrowed_quantity': 29, 'borrowed_at': datetime(2024, 1, 5, 15, 57, 29), 'returned': False},
    {'user_id': 22239, 'role': 'teacher', 'username': 'Charlene Rainon', 'item_id': 7241, 'item_name': 'markers', 'item_description': 'Handcrafted masterpiece', 'borrowed_quantity': 53, 'borrowed_at': datetime(2024, 1, 2, 18, 34, 45), 'returned': False},
    {'user_id': 22477, 'role': 'student', 'username': 'Zed Straffon', 'item_id': 2829, 'item_name': 'folders', 'item_description': 'Limited edition piece', 'borrowed_quantity': 38, 'borrowed_at': datetime(2024, 1, 10, 2, 18, 4), 'returned': False},
    {'user_id': 22394, 'role': 'student', 'username': 'Hebert Balharry', 'item_id': 6681, 'item_name': 'glue sticks', 'item_description': 'High-quality item', 'borrowed_quantity': 60, 'borrowed_at': datetime(2024, 1, 6, 20, 24, 12), 'returned': True},
    {'user_id': 22230, 'role': 'teacher', 'username': 'Briant Snawden', 'item_id': 3910, 'item_name': 'glue sticks', 'item_description': 'Vintage collectible', 'borrowed_quantity': 21, 'borrowed_at': datetime(2024, 1, 1, 7, 29, 29), 'returned': False},
    {'user_id': 22418, 'role': 'student', 'username': 'Roxie Sterley', 'item_id': 7612, 'item_name': 'rulers', 'item_description': 'Vintage collectible', 'borrowed_quantity': 27, 'borrowed_at': datetime(2024, 1, 5, 14, 58, 23), 'returned': False},
    {'user_id': 22051, 'role': 'teacher', 'username': 'Garv Britzius', 'item_id': 7819, 'item_name': 'binders', 'item_description': 'Handcrafted masterpiece', 'borrowed_quantity': 19, 'borrowed_at': datetime(2024, 1, 3, 1, 41, 23), 'returned': False},
    {'user_id': 22469, 'role': 'teacher', 'username': 'Callie Bromige', 'item_id': 9636, 'item_name': 'notebooks', 'item_description': 'Limited edition piece', 'borrowed_quantity': 50, 'borrowed_at': datetime(2024, 1, 6, 22, 26, 3), 'returned': True},
    {'user_id': 22142, 'role': 'teacher', 'username': 'Guillaume Marden', 'item_id': 7948, 'item_name': 'folders', 'item_description': 'High-quality item', 'borrowed_quantity': 25, 'borrowed_at': datetime(2024, 1, 1, 12, 14, 41), 'returned': False},
    {'user_id': 22071, 'role': 'student', 'username': 'Pebrook Bourdis', 'item_id': 6185, 'item_name': 'pencils', 'item_description': 'Limited edition piece', 'borrowed_quantity': 15, 'borrowed_at': datetime(2024, 1, 2, 7, 48, 24), 'returned': False},
    {'user_id': 22428, 'role': 'student', 'username': 'Darryl Stickells', 'item_id': 5046, 'item_name': 'rulers', 'item_description': 'High-quality item', 'borrowed_quantity': 1, 'borrowed_at': datetime(2024, 1, 9, 10, 29, 8), 'returned': True},
    {'user_id': 22381, 'role': 'student', 'username': 'Anjela Kornilyev', 'item_id': 6668, 'item_name': 'folders', 'item_description': 'Limited edition piece', 'borrowed_quantity': 46, 'borrowed_at': datetime(2024, 1, 6, 1, 33, 40), 'returned': False},
    {'user_id': 22437, 'role': 'student', 'username': 'Teddi Baile', 'item_id': 5458, 'item_name': 'erasers', 'item_description': 'High-quality item', 'borrowed_quantity': 44, 'borrowed_at': datetime(2024, 1, 7, 7, 13, 45), 'returned': True},
    {'user_id': 22340, 'role': 'student', 'username': 'Janenna Antonowicz', 'item_id': 8199, 'item_name': 'folders', 'item_description': 'Handcrafted masterpiece', 'borrowed_quantity': 25, 'borrowed_at': datetime(2024, 1, 1, 10, 55, 41), 'returned': True},
    {'user_id': 22428, 'role': 'teacher', 'username': 'Issie Deaconson', 'item_id': 6126, 'item_name': 'scissors', 'item_description': 'High-quality item', 'borrowed_quantity': 22, 'borrowed_at': datetime(2024, 1, 8, 10, 14, 41), 'returned': True},
    {'user_id': 22470, 'role': 'teacher', 'username': 'Julissa Pealing', 'item_id': 3095, 'item_name': 'rulers', 'item_description': 'Vintage collectible', 'borrowed_quantity': 54, 'borrowed_at': datetime(2024, 1, 5, 8, 0, 53), 'returned': False},
    {'user_id': 22101, 'role': 'teacher', 'username': 'Quill Jennaroy', 'item_id': 4433, 'item_name': 'folders', 'item_description': 'Limited edition piece', 'borrowed_quantity': 54, 'borrowed_at': datetime(2024, 1, 6, 6, 56, 34), 'returned': False},
    {'user_id': 22230, 'role': 'teacher', 'username': 'Nappie Rodolico', 'item_id': 3552, 'item_name': 'binders', 'item_description': 'High-quality item', 'borrowed_quantity': 19, 'borrowed_at': datetime(2024, 1, 5, 22, 45, 10), 'returned': True},
    {'user_id': 22106, 'role': 'student', 'username': 'Hussein Josifovic', 'item_id': 6911, 'item_name': 'scissors', 'item_description': 'Handcrafted masterpiece', 'borrowed_quantity': 16, 'borrowed_at': datetime(2024, 1, 9, 10, 8, 50), 'returned': True},
    {'user_id': 22355, 'role': 'teacher', 'username': 'Zane Mangeney', 'item_id': 3100, 'item_name': 'notebooks', 'item_description': 'High-quality item', 'borrowed_quantity': 41, 'borrowed_at': datetime(2024, 1, 5, 17, 22, 9), 'returned': False},
    {'user_id': 22184, 'role': 'teacher', 'username': 'Krystyna Brownscombe', 'item_id': 2161, 'item_name': 'markers', 'item_description': 'High-quality item', 'borrowed_quantity': 33, 'borrowed_at': datetime(2024, 1, 10, 9, 27, 20), 'returned': True},
    {'user_id': 22252, 'role': 'student', 'username': 'Luise Bush', 'item_id': 8407, 'item_name': 'binders', 'item_description': 'Handcrafted masterpiece', 'borrowed_quantity': 5, 'borrowed_at': datetime(2024, 1, 3, 22, 53, 19), 'returned': True},
    {'user_id': 22303, 'role': 'teacher', 'username': 'Bertine Rottery', 'item_id': 5350, 'item_name': 'calculators', 'item_description': 'Vintage collectible', 'borrowed_quantity': 43, 'borrowed_at': datetime(2024, 1, 8, 20, 49, 18), 'returned': False},
    {'user_id': 22386, 'role': 'student', 'username': 'Grace Eate', 'item_id': 8573, 'item_name': 'binders', 'item_description': 'Handcrafted masterpiece', 'borrowed_quantity': 12, 'borrowed_at': datetime(2024, 1, 2, 5, 31, 26), 'returned': True},
    {'user_id': 22258, 'role': 'teacher', 'username': 'Roanne Wyvill', 'item_id': 7991, 'item_name': 'glue sticks', 'item_description': 'Limited edition piece', 'borrowed_quantity': 9, 'borrowed_at': datetime(2024, 1, 8, 20, 56, 19), 'returned': True},
    {'user_id': 22387, 'role': 'teacher', 'username': 'Hanny Olpin', 'item_id': 1561, 'item_name': 'glue sticks', 'item_description': 'Vintage collectible', 'borrowed_quantity': 11, 'borrowed_at': datetime(2024, 1, 8, 9, 49, 19), 'returned': True},
    {'user_id': 22292, 'role': 'teacher', 'username': 'Mildrid Doding', 'item_id': 2394, 'item_name': 'rulers', 'item_description': 'Handcrafted masterpiece', 'borrowed_quantity': 7, 'borrowed_at': datetime(2024, 1, 10, 22, 19, 18), 'returned': True},
    {'user_id': 22130, 'role': 'teacher', 'username': 'Chrissie Monson', 'item_id': 4520, 'item_name': 'binders', 'item_description': 'High-quality item', 'borrowed_quantity': 45, 'borrowed_at': datetime(2024, 1, 1, 5, 32, 23), 'returned': True},
    {'user_id': 22268, 'role': 'teacher', 'username': 'Sarena Wollard', 'item_id': 8782, 'item_name': 'notebooks', 'item_description': 'Handcrafted masterpiece', 'borrowed_quantity': 34, 'borrowed_at': datetime(2024, 1, 8, 15, 8, 4), 'returned': True},
    {'user_id': 22452, 'role': 'student', 'username': 'Lawrence Fellgett', 'item_id': 6813, 'item_name': 'erasers', 'item_description': 'High-quality item', 'borrowed_quantity': 23, 'borrowed_at': datetime(2024, 1, 11, 19, 26, 36), 'returned': True},
    {'user_id': 22195, 'role': 'teacher', 'username': 'Brucie Carwithen', 'item_id': 6509, 'item_name': 'rulers', 'item_description': 'Vintage collectible', 'borrowed_quantity': 33, 'borrowed_at': datetime(2024, 1, 5, 14, 38, 27), 'returned': False},
    {'user_id': 22418, 'role': 'student', 'username': 'Betti MacPaden', 'item_id': 5819, 'item_name': 'scissors', 'item_description': 'High-quality item', 'borrowed_quantity': 51, 'borrowed_at': datetime(2024, 1, 10, 12, 13, 45), 'returned': False}
]

with app.app_context():
    # Drop all tables and create them again
    db.drop_all()
    db.create_all()

    # Seed users
    for user_data in users_data:
        user = User(username=user_data['username'], role=user_data['role'])
        user.set_password(user_data['password'])  # Use set_password to hash the password
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
