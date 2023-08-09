from dotenv import load_dotenv
load_dotenv()

# Regardless of the lint error you receive,
# load_dotenv must run before running this
# so that the environment variables are
# properly loaded.
from app import app, db
from app.models import Employee, Menu, MenuItem, MenuItemType, Table, Order, Order_Items


with app.app_context():
    db.drop_all()
    db.create_all()

    employee = Employee(name="Margot", employee_number=1234, password="password")
    db.session.add(employee)
    db.session.commit()
    beverages = MenuItemType(name="Beverages")
    entrees = MenuItemType(name="Entrees")
    sides = MenuItemType(name="Sides")

    dinner = Menu(name="Dinner")

    fries = MenuItem(name="French fries", price=3.50, menu_type_id=3, menu_id=1)
    drp = MenuItem(name="Dr. Pepper", price=1.0, menu_type_id=1, menu_id=1)
    jambalaya = MenuItem(name="Jambalaya", price=21.98, menu_type_id=2, menu_id=1)
    db.session.add_all([beverages, entrees, sides, dinner, fries, drp, jambalaya])
    db.session.commit()

    #  Create tables
    tables = []
    for i in range(10):
        tables.append(Table(capacity=(i*2), number=(i*3)))
    db.session.add_all(tables)
    db.session.commit()

    # create an order
    new_order = Order( server=1, table=1)
    new_order_items1 = Order_Items(orderId=1, itemId=1)
    new_order_items2= Order_Items(orderId=1, itemId=2)
    new_order_items3 = Order_Items(orderId=1, itemId=3)
    db.session.add_all([new_order, new_order_items1, new_order_items2, new_order_items3])
    db.session.commit()
