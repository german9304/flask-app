from flask import (
    request, views, redirect, jsonify, make_response
)
from shopcart.models import (
    productSchema, 
    userSchema, 
    product, 
    user, 
    review, 
    db,
    reviewsSchema
)
from sqlalchemy import desc, exc
import json
import functools

def handler_404(func):
    @functools.wraps(func)
    def wrap_func(*params, **kwargs):
        try:
            res = func(*params, **kwargs)
            return res
        except (exc.SQLAlchemyError, Exception) as e:
            # print(str(e))
            resp = {'success': False, 'data': str(e)}
            header = {'content-type': 'application/json'}
            res = (json.dumps(resp), 404, header)
            return make_response(res)

    return wrap_func


class ProductsAPI(views.MethodView):
    """Products RESTful API."""

    @handler_404
    def get(self, product_id=None):
        """HTTP GET method."""

        if product_id:
            product_data = product.Product.query \
                .filter(product.Product.id == product_id).first_or_404()
            serialize_product = productSchema.PRODUCT_SCHEMA \
                    .dump(product_data)
            return jsonify(data=serialize_product.data)

        products_data = product.Product.query.all()
        serialize_products = productSchema.PRODUCTS_SCHEMA.dump(products_data)
        return jsonify(data=serialize_products)

    @handler_404
    def post(self, product_id):
        """HTTP POST method."""
        res = request.json['comment']
        user_id = 2
        rev = review.Reviews(product_id=product_id, user_id=user_id, 
                comment=res)
        review_data = db.database.insert(rev)
        serialize_review = reviewsSchema.REVIEW_SCHEMA.dump(review_data)
        return jsonify(data=serialize_review)

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



#     try:
#         product_data = product.Product.query. \
#             filter(product.Product.id == product_id).one()
#         res = productSchema.PRODUCT_SCHEMA \
#                 .dump(product_data)
#         return jsonify(data=res.data, errors=res.errors)
#     except (exc.SQLAlchemyError, Exception) as e:
#         # print(type(e))
#         resp = {'success':False, 'data': ''}
#         header = {'content-type': 'application/json'}
#         res = (json.dumps(resp), 404, header)
#         return make_response(res)