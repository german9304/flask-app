from flask_sqlalchemy import SQLAlchemy
from .dbconfig import POSTGRES


class SqlAlchemy():
    """Database configuration."""
    
    def __init__(self, db = '', uri = ''):
        self.db = db
        self.uri = uri

    def init_db(self, app):
        url = self.init_db_info(POSTGRES)
        app.config['SQLALCHEMY_DATABASE_URI'] = url
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        self.db = SQLAlchemy(app)

    def init_db_info(self, db):
        USER = POSTGRES['USER']
        PWD = POSTGRES['PW']
        DB = POSTGRES['DB']
        url = f'postgresql://{USER}:{PWD}@localhost/{DB}'
        return url

    def get_db(self):
        return self.db


db = SqlAlchemy()

