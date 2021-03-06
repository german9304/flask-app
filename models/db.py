from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from .dbconfig import POSTGRES


class Database():
    """Database configuration."""
    
    def __init__(self):
        self.database = SQLAlchemy()
        self.uri = ''
        self.ma = Marshmallow()

    def init_db(self, app):
        """Initialize db."""
        self.init_db_info(POSTGRES)
        app.config['SQLALCHEMY_DATABASE_URI'] = self.uri
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        self.database.init_app(app) # init flask alchemy
        self.ma.init_app(app) # init flask marshmellow

    def init_db_info(self, postgres):
        """Init database info."""
        user = postgres['USER']
        pwd = postgres['PW']
        database = postgres['DB']
        url = f'postgresql://{user}:{pwd}@localhost/{database}'
        self.uri = url
        return url

    def get_db(self):
        """Returns database."""
        return self.database
    
    def get_ma(self):
        return self.ma
    
    def insert(self, row):
        db = self.get_db()
        try:
            db.session.add(row)
            db.session.commit()
        except Exception as e:
            print(e)
            print('ann error ocurred')
        return row
    def commit_changes(self):
        return self.database.session.commit()

database = Database()



