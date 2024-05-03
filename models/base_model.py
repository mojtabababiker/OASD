"""
Base model which define some common attributes and methods for the rest of app models
"""
import uuid
from datetime import datetime
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

    def __init__(self, *args, **kwargs):  # pylint: disable=unused-argument
        """
        initiate the class attributes
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

        # self.save()

    def save(self):
        """
        add the current record to the session
        """
        from app import app  # pylint: disable=import-outside-toplevel

        with app.app_context():
            db.session.add(self)
            db.session.commit()

    def delete(self):
        """
        delete the record from the session and commit the change
        """
        from app import app  # pylint: disable=import-outside-toplevel

        with app.app_context():
            db.session.delete(self)
            db.session.commit()

    # def to_dict(self):
    #     """
    #     create and return costumize dictionry of the instance
    #     """
