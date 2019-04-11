from flask import (
    request, views, redirect, jsonify, make_response
)
from shopcart.models import (
    productSchema, userSchema, product, user
)
from sqlalchemy import desc, exc
import json
import functools

def handler_404(func):
    @functools.wraps(func)
    def wrap_func(*params, **kwargs):
        res = func(*params, **kwargs)
        print(res)
        return func(*params, **kwargs)
    return wrap_func


class ProductsAPI(views.MethodView):
    """Products RESTful API."""

    def get_product(self, product_id):
        try:
            resp = product.Product.query.get(product_id)
        except (exc.SQLAlchemyError, Exception) as e:
            print(e)
            # return make_response()
            return jsonify({'user':'user'})
        # print(resp)
        return resp
    
    # @handler_404
    def get(self, product_id=None):
        """HTTP GET method."""

        if product_id:
            print(product_id)
            data = self.get_product(product_id)
            if data:
                res = productSchema.PRODUCT_SCHEMA \
                        .dump(data)
                # print(type(data))
                return jsonify(data=res.data, errors=res.errors)
            else:
                data = {'success':False, 'data':'user not found'}
                header = {'content-type': 'application/json'}
                res = (json.dumps(data), 404, header)
                return make_response(res)

        products = product.Product.query.all()
        data = productSchema.PRODUCTS_SCHEMA.dump(products)
        return jsonify(products=data)

    def post(self, product_id):
        """HTTP POST method."""
        res = request.json
        print(res)
        
        return jsonify(name='john', age=32)

    def put(self):
        """HTTP PUT METHOD."""
        pass
    
    def delete(self):
        """HTTP DELETE METHOD."""
        pass


def register_product_api(app, endpoint, url='/api/products'):
    """Registers endpoint for user api."""
    view_func = ProductsAPI.as_view(endpoint)
    app.add_url_rule(url, view_func=view_func,
                    methods=['GET'])
    app.add_url_rule('/api/product/<int:product_id>/', view_func=view_func, 
                    methods=['POST', 'PUT', 'DELETE', 'GET'])
