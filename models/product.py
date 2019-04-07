"""
This module contains
the class for products model
"""
from .db import database
from sqlalchemy import ForeignKey
from .likes import Likes
# from .review import Reviews

model = database.get_db()


class Product(model.Model):
    """Product model."""
    __tablename__= 'product'
    id = model.Column(model.Integer, primary_key=True)
    name = model.Column(model.String(120), nullable=False)
    likes = model.Column(model.Integer, default=0)
    description = model.Column(model.String(200), nullable=False)
    quantity = model.Column(model.Integer, nullable=False)
    user_id = model.Column(model.Integer, ForeignKey('users.id'),
                           nullable=False)
    likes_assoc = model.relationship('Likes', back_populates='product_parent')
    reviews_assoc = model.relationship('Reviews', back_populates='product_parent')

    def get_name(self):
        return self.name
