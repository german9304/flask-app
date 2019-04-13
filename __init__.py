from flask import Flask
from .views.main import homeBP
from .views import (
    stores, auth
)
from .models.dbconfig import key
from .api import products, users, review

def create_app():
    app = Flask(__name__)
    from .models.db import database
    database.init_db(app)
    app.secret_key = key
    app.register_blueprint(auth.authBp)
    app.register_blueprint(stores.storesBp)
    app.add_url_rule('/', endpoint='home')
    products.register_product_api(app, 'api-products')
    users.register_user_api(app, 'api-users')
    review.register_review_api(app, 'api-reviews')
    return app