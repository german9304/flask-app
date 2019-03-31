"""
This module contains
the class for user model
"""
from .db import database


model = database.get_db()


class Users(model.Model):
    """User model."""
    id = model.Column(model.Integer, primary_key=True)
    email = model.Column(model.String(120), unique=True, nullable=False)
    username = model.Column(model.String(120), unique=True, nullable=False)
    products = model.relationship('Product', backref='users')

    def get_products(self):
        return self.products
