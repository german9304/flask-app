from flask import (
    request, views, redirect, jsonify, session
)
from shopcart.models import (
    productSchema, userSchema, product, user, review, reviewsSchema
)


class UsersAPI(views.MethodView):
    """Products RESTful API."""

    def get(self, get_user):
        """HTTP GET method."""
        if get_user:
            if 'username' in session:
                user_id = session['username']
                user_data = user.Users.query.get(user_id)
                serialize_user = userSchema.USER_SCHEMA.dump(user_data)
                serialized = serialize_user.data
                res_user = {
                    'id': serialized['id'],
                    'username': serialized['username'],
                    'email' : serialized['email']
                }
                return jsonify(data=res_user, succes=True)
            else:
                return jsonify(data='user not authenticated', success=False)

        users = user.Users.query.all()
        users_data = userSchema.USERS_SCHEMA.dump(users)
        return jsonify(users_data.data)

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
    app.add_url_rule(url, view_func=view_func, defaults={'get_user': None},
        methods=['GET'])
    app.add_url_rule('/api/user/', view_func=view_func, 
        defaults={'get_user': True}, methods=['GET'])