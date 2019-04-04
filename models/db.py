from flask_sqlalchemy import SQLAlchemy
from .dbconfig import POSTGRES


class Database():
    """Database configuration."""
    
    def __init__(self):
        self.database = SQLAlchemy()
        self.uri = ''

    def init_db(self, app):
        """Initialize db."""
        self.init_db_info(POSTGRES)
        app.config['SQLALCHEMY_DATABASE_URI'] = self.uri
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        self.database.init_app(app)

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

database = Database()


