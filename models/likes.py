"""
This module contains
the class for user model
"""
from .db import database
from datetime import date
# from .user import Users
# from .product import Product
from sqlalchemy import (
    ForeignKey
)

model = database.get_db()


# user_product_likes = model.Table('likes', 
#     model.Column('user_id', ForeignKey('users.id'), primary_key=True),
#     model.Column('product_id', ForeignKey('product.id'), primary_key=True),
#     model.Column('liked_on', model.DateTime, default=date.today(), primary_key=True)
# )

class Likes(model.Model):
    """Likes Association Table."""
    __tablename__= 'likes'
    id = model.Column(model.Integer, primary_key=True)
    product_id = model.Column(model.Integer, ForeignKey('product.id'),
                           nullable=False)
    user_id = model.Column(model.Integer, ForeignKey('users.id'),
                           nullable=False)
    liked_on = model.Column(model.DateTime, default=date.today(), nullable=False)
    user_parent = model.relationship('Users', back_populates="likes_assoc")
    product_parent = model.relationship('Product', back_populates='likes_assoc')
