"""
This module contains
the class for products model
"""
from .db import database
from sqlalchemy import ForeignKey


model = database.get_db()


class Product(model.Model):
    """Porduct model."""
    id = model.Column(model.Integer, primary_key=True)
    name = model.Column(model.String(120), nullable=False)
    likes = model.Column(model.Integer, nullable=False, default=0)
    description = model.Column(model.String(200), nullable=False)
    quantity = model.Column(model.Integer, nullable=False)
    user_id = model.Column(model.Integer, ForeignKey('users.id'),
                           nullable=False)

    def get_name(self):
        return self.name
