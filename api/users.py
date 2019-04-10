from flask import (
    request, views, redirect, jsonify
)
from shopcart.models import (
    productSchema, userSchema
)

from ..models import (
    product, user
)


class UsersAPI(views.MethodView):
    """Products RESTful API."""

    def get(self):
        """HTTP GET method."""
        users = user.Users.query.all()
        data = userSchema.USERS_SCHEMA.dump(users)
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