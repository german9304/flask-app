from flask import (
    request, views, redirect, jsonify
)


class ProductsAPI(views.MethodView):
    """Products RESTful API."""

    def get(self):
        """HTTP GET method."""
        return jsonify(name='john')

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