"""
This module contains
the class for user model
"""
from .db import database


model = database.get_db()

class Users(model.Model):
    id = model.Column(model.Integer, primary_key=True)
    email = model.Column(model.String(20), unique=True, nullable=False)
    username = model.Column(model.String(20), unique=True, nullable=False)


