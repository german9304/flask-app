from .db import database
from . import user
from shopcart.models import productSchema

ma = database.get_ma()


class UsersSchema(ma.ModelSchema):
    """Schema representation of User."""
    class Meta:
        model = user.Users

    products = ma.Nested('ProductSchema', many=True, exclude=('users', ))


USERS_SCHEMA = UsersSchema(many=True)
USER_SCHEMA = UsersSchema()

# schema = productSchema.ProductSchema

