"""
set up the database connection
"""
from os import getenv
from sqlalchemy.engine.url import URL
from flask_sqlalchemy import SQLAlchemy

class DBStorage(SQLAlchemy):
    """
    class the represents an upstract for database storage oprations
    whic inherits from the SQLAlchemy class
    """
    __db_user = getenv("DB_USER")
    __db_psswd = getenv("DB_PSSWD")
    __db_host = getenv("DB_HOST")
    __db_port = getenv("DB_PORT")
    __db_name = getenv("DB_NAME")

    url = URL.create("mysql+mysqldb",
                username=__db_user,
                password=__db_psswd,
                host=__db_host,
                port=__db_port,
                database=__db_name)

    def __init__(self):
        """
        init the database storage apstarction
        """
        super().__init__()
        self._app = None

    # override the SQLAlchemy init_app method
    def init_app(self, app):
        """
        set app to self._app and call super init_app method
        """
        self._app = app
        super().init_app(app)
        
    def create_tables(self):
        """
        create all the database tables
        """
        from models.admins_model import Admin
        from models.articals_model import Artical
        from models.job_offers_model import JobOffer

        with self._app.app_context():
            self.create_all()
