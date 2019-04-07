"""
This module contains
the class for user model
"""
from .db import database
from sqlalchemy.orm import backref
# from .product import Product
# from .likes import Likes
from .review import Reviews

model = database.get_db()


class Users(model.Model):
    """User model."""
    id = model.Column(model.Integer, primary_key=True)
    email = model.Column(model.String(120), unique=True, nullable=False)
    username = model.Column(model.String(120), unique=True, nullable=False)
    password = model.Column(model.String(20), nullable=False, default='test')
    products = model.relationship('Product', backref='users',  
        cascade="all, delete" ,lazy=True)
    likes_assoc = model.relationship('Likes', back_populates='user_parent')
    reviews_assoc = model.relationship('Reviews', back_populates='user_parent')

    def get_products(self):
        return self.products
    
    def get_password(self):
        return self.password
    
    def get_username(self):
        return self.username

    def get_porducts(self):
        return self.products

    def get_Id(self):
        return self.id

    
