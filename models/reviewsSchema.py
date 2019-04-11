from .db import database
from shopcart.models import review
from . import product
from marshmallow import fields
from shopcart.models import userSchema, productSchema
# from . import user_init


ma = database.get_ma()


class ReviewSchema(ma.ModelSchema):
    """Review Schema."""
    class Meta:
        model = review.Reviews

    user_parent = ma.Nested('UsersSchema', only=('username', 'id', 'email'))
    product_parent = ma.Nested('ProductSchema', 
            only=('name', 'description', 'id'))

    
REVIEWS_SCHEMA = ReviewSchema(many=True)
REVIEW_SCHEMA = ReviewSchema()