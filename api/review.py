from flask import (
    request, views, redirect, jsonify, session
)
from shopcart.models import (
    db, productSchema, userSchema, product, user, review, reviewsSchema
)


class ReviewAPI(views.MethodView):

    def get(self):
        reviews = review.Reviews.query.all()
        serialized_data = reviewsSchema.REVIEWS_SCHEMA.dump(reviews)
        return jsonify(review=serialized_data.data)

    def post(self):
        """Create Review."""
        user = None
        try:
            if 'username' in session:
                user_id = session['username']
                comment = request.json['comment']
                product_id = request.json['product']
                rev = review.Reviews(product_id=product_id, user_id=user_id, comment=comment)
                review_data = db.database.insert(rev)
                serialize_review = reviewsSchema.REVIEW_SCHEMA.dump(review_data)
                return jsonify(data=serialize_review.data)
        except Exception as e:
            return jsonify(success=False)


def register_review_api(app, endpoint, url='/api/reviews'):
    view_func = ReviewAPI.as_view(endpoint)
    app.add_url_rule(url, view_func=view_func, methods=['GET'])
    app.add_url_rule('/api/review/', view_func=view_func, methods=['POST'])