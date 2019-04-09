from .db import database
from . import product

ma = database.get_ma()


class productSchema(ma.ModelSchema):
    class Meta:
        model = product.Product


products_schema = productSchema(many=True)
product_schema = productSchema()