from flask import (
    request, views, redirect, jsonify
)

from ..models import (
    product, productSchema as pschema
)

class ProductsAPI(views.MethodView):
    """Products RESTful API."""

    def get(self):
        """HTTP GET method."""
        products = product.Product.query.all()
        data = pschema.products_schema.dump(products)
        return jsonify(data)

    def post(self):
        """HTTP POST method."""
        return jsonify(name='john', age=32)

    def put(self):
        """HTTP PUT METHOD."""
        pass
    
    def delete(self):
        """HTTP DELETE METHOD."""
        pass


def register_api():
    return ''