from flask import Flask
from .views.main import homeBP


def create_app():
    app = Flask(__name__)
    app.register_blueprint(homeBP)
    return app
