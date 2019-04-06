from flask import Flask
from .views.main import homeBP
from .views import (
    stores, auth
)
from .models.dbconfig import key


def create_app():
    app = Flask(__name__)
    from .models.db import database
    database.init_db(app)
    app.secret_key = key
    app.register_blueprint(auth.authBp)
    app.register_blueprint(stores.storesBp)
    app.add_url_rule('/', endpoint='home')
    return app