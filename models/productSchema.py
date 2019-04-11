
from .db import database
from shopcart.models import userSchema, reviewsSchema
from . import product
from marshmallow import fields

# from . import user_init


ma = database.get_ma()


class ProductSchema(ma.ModelSchema):
    """Schema representation of Product."""
    class Meta:
        model = product.Product
        # exclude=('likes_assoc', 'products', 'reviews_assoc', )
    users = fields.Nested('UsersSchema', only=('email', 'id', 'username', ))
    reviews_assoc = ma.Nested('ReviewSchema', many=True, 
        exclude=('product_parent', ))

PRODUCTS_SCHEMA = ProductSchema(many=True)
PRODUCT_SCHEMA = ProductSchema()

