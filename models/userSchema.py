from .db import database
from . import user
from shopcart.models import productSchema, reviewsSchema
from marshmallow import fields

ma = database.get_ma()


class UsersSchema(ma.ModelSchema):
    """Schema representation of User."""
    class Meta:
        fields = ('email', 'username', 'products')

    products = ma.Nested('ProductSchema', many=True, exclude=('users', ))
    reviews_assoc = ma.Nested('ReviewSchema', many=True, 
        only=('id', 'comment', 'created_on', 'user_parent'))


USERS_SCHEMA = UsersSchema(many=True)
USER_SCHEMA = UsersSchema()

# schema = productSchema.ProductSchema

