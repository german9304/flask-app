"""
This module contains
the class for user model
"""
from .db import database
from sqlalchemy.orm import backref

model = database.get_db()


class Users(model.Model):
    """User model."""
    id = model.Column(model.Integer, primary_key=True)
    email = model.Column(model.String(120), unique=True, nullable=False)
    username = model.Column(model.String(120), unique=True, nullable=False)
    password = model.Column(model.String(20), nullable=False, default='test')
    products = model.relationship('Product', backref='users',  cascade="all, delete" ,lazy=True)

    def get_products(self):
        return self.products
