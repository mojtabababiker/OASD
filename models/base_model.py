"""
Base model which define some common attributes and methods for the rest of app models
"""
import uuid
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

from models import db


class BaseModel:
    """
    Base model class thaat define common attributes and methos for the rest of
    app models, such as id, creatation and modification time atrributes
    """
    id = db.Column(db.String(60),
                    primary_key=True,
                    nullable=False)
    created_at = db.Column(db.DateTime,
                    default=datetime.utcnow,
                    nullable=False)
    updated_at = db.Column(db.DateTime,
                    default=datetime.utcnow,
                    nullable=False)

    def __init__(self, *args, **kwargs):
        """
        initiate the class attributes
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    # def __str__(self):
    #     """
    #     Costumize the magic method __str__
    #     """
    #     return f"{self.__class__.__name__}.{self.id} {self.to_dict()}"

    # def to_dict(self):
    #     """
    #     create and return costumize dictionry of the instance
    #     """
        