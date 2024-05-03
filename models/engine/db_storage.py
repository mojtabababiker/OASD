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
    db_user = getenv("DB_USER")
    db_psswd = getenv("DB_PSSWD")
    db_host = getenv("DB_HOST")
    db_name = getenv("DB_NAME")

    # url = URL.create("mysql",
    #             username=__db_name,
    #             password=__db_psswd,
    #             host=__db_host,
    #             port=3306,
    #             database=__db_name)

    def __inti__(self, app):
        """
        init the database storage apstarction
        """
        print(self.url)

    def create_tables(self, app):
        from models.admins_model import Admin
        from models.articals_model import Artical
        from models.job_offers_model import JobOffer
        with app.app_context():
            self.drop_all()
            self.create_all()

        # admin = Admin("Mojtaba", 'Mohammed', 'mojmohammad98@gmail.com', 'tabo0901267500')
        # admin.save()