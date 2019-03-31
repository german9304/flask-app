from flask import Flask
from .views.main import homeBP
from .views.stores import storesBp
from .models.db import db

def create_app():
    app = Flask(__name__)
    db.init_db(app) # init database config
    app.register_blueprint(storesBp)

    return app
