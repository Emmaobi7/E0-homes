"""
db models
sqlalchemy with mysql
"""

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean, Table
from flask_login import UserMixin
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime


Base = declarative_base()


combine_pc = Table('combine_pc', Base.metadata,
    Column('cart_id', Integer, ForeignKey('cart.id')),
    Column('product_id', Integer, ForeignKey('products.id'))
)

class User(Base, UserMixin):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50))
    email = Column(String(50), nullable=False, unique=True)
    password = Column(String(300), nullable=False)
    state = Column(String(20))
    city = Column(String(50))
    product = relationship("Product", back_populates="user")
    order = relationship("Order", back_populates="user", uselist=False)
    cart = relationship('Cart', back_populates='user', uselist=False)
    review = relationship('Review', back_populates='user')


class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    title = Column(String(500), nullable=False)
    category = Column(String(500), nullable=False)
    description = Column(String(5000), nullable=False)
    image = Column(String(500))
    status = Column(Boolean, nullable=True)
    price = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="product")
    carts = relationship("Cart", secondary=combine_pc, back_populates="products")


class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    status = Column(Boolean, nullable=False)
    date = Column(DateTime, default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="order")

class Cart(Base):
    __tablename__ = 'cart'
    id = Column(Integer, primary_key=True)
    quantity = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='cart')
    products = relationship("Product", secondary=combine_pc, back_populates="carts")


class Agent(Base):
    __tablename__ = 'agents'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    location = Column(String(50), nullable=False)
    status = Column(Boolean, nullable=False)

class Review(Base):
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    content = Column(String(100))
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='review')

# class ProductCart(Base):
#     __tablename__ = 'combine_pc'
#     product_id = Column(Integer, ForeignKey('products.id'), primary_key=True)
#     cart_id = Column(Integer, ForeignKey('cart.id'), primary_key=True)
