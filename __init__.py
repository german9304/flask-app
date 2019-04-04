from flask import Flask
from .views.main import homeBP
from .views.stores import storesBp

def create_app():
    app = Flask(__name__)
    from .models.db import database
    database.init_db(app)
    app.register_blueprint(storesBp)
    return app