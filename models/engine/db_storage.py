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

    url = URL("mysql+mysqldb",
                username=__db_name,
                password=__db_psswd,
                host=__db_host,
                port=__db_port,
                database=__db_name)

    def __inti__(self, app):
        """
        init the database storage apstarction
        """
        super().__init__()
        
    def create_tables(self):
        from models.admins_model import Admin
        from models.atricals_model import Artical
        from models.job_offers_model import JobOffer

        self.create_all()

    