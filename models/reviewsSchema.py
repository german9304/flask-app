from .db import database
from shopcart.models.review import Reviews
from . import product
from marshmallow import fields

# from . import user_init


ma = database.get_ma()


class ReviewSchema(ma.ModelSchema):
    class Meta:
        model = Reviews
    