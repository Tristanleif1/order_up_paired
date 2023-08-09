from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Integer, String, Float
from sqlalchemy.orm import relationship

db = SQLAlchemy()

class Employee(db.Model, UserMixin):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    employee_number = Column(Integer, nullable=False, unique=True)
    hashed_password = Column(String(255), nullable=False)
    orders = relationship('Order', back_populates='employee')
    @property
    def password(self):
        return self.hashed_password

    @password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

class Menu(db.Model, UserMixin):
    __tablename__ = 'menus'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False)

class MenuItem(db.Model, UserMixin):
    __tablename__ = 'menuItems'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    price = Column(Float, nullable=False)
    menu_id = Column(Integer, ForeignKey('menus.id'), nullable=False)
    menu_type_id = Column(Integer, ForeignKey('menuItemTypes.id'), nullable=False)

class MenuItemType(db.Model, UserMixin):
    __tablename__ = 'menuItemTypes'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False)

class Table(db.Model):
    __tablename__ = 'tables'
    id = Column(Integer, primary_key=True, autoincrement=True)
    number = Column(Integer, nullable=False, unique=True)
    capacity = Column(Integer, nullable=False)

class Order(db.Model):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True, autoincrement=True)
    server = Column(Integer, ForeignKey('employees.id'), nullable=False)
    table = Column(Integer, ForeignKey('tables.id'), nullable=False)
    bill_paid = Column(String(10), default='false', nullable=False)
    employee = relationship('Employee', back_populates='orders')
    #  FIX THIS
    employee = relationship('Employee', back_populates='orders')

class Order_Items(db.Model):
    __tablename__ = 'orderItems'
    id = Column(Integer, primary_key=True, autoincrement=True)
    orderId = Column(Integer, ForeignKey('orders.id'))
    itemId = Column(Integer, ForeignKey('menuItems.id'))
