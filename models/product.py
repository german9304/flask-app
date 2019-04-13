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
    user_id = model.Column(model.Integer, ForeignKey('users.id'), nullable=False)
    likes_assoc = model.relationship('Likes', back_populates='product_parent')
    reviews_assoc = model.relationship('Reviews', back_populates='product_parent')

    def get_name(self):
        """Returns product name."""
        return self.name
    
    def get_store_id(self):
        """Returns store id."""
        return self.id
    
    def get_reviews(self):
        """Returns product by user reviews."""
        return self.reviews_assoc
    
    def get_likes(self):
        """Returns who liked the product."""
        return self.likes_assoc
