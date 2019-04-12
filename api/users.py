from flask import (
    request, views, redirect, jsonify
)
from shopcart.models import (
    productSchema, userSchema, product, user, review, reviewsSchema
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


def register_user_api(app, endpoint, url='/api/users'):
    view_func = UsersAPI.as_view(endpoint)
    app.add_url_rule(url, view_func=view_func, methods=['GET'])