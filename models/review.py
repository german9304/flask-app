"""
This module contains
the class for user model
"""
from .db import database
from datetime import date
# from .product import Product
# from .user import Users
# from .review import review
from sqlalchemy import (
    ForeignKey
)

model = database.get_db()

class Reviews(model.Model):
    """Reviews Association Table."""
    __tablename__='reviews'
    id = model.Column(model.Integer, primary_key=True)
    product_id = model.Column(model.Integer, ForeignKey('product.id'), nullable=False)
    user_id = model.Column(model.Integer, ForeignKey('users.id'), nullable=False)
    comment = model.Column(model.String(200), nullable=False)
    created_on = model.Column(model.DateTime, default=date.today(), nullable=False)
    user_parent = model.relationship('Users', back_populates='reviews_assoc')
    product_parent = model.relationship('Product', back_populates='reviews_assoc')

    def get_comment(self):
        return self.comment

    def get_user(self):
        return self.user_parent
    
