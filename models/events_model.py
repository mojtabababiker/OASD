from models import db
from models.articals_model import Artical


class Event(Artical):
    """
    Event model which subclassing the Artical model, and add extra column and method
    """

    __tablename__ = "events"

    date = db.Column(db.DateTime,
                        nullable=False)

    location = db.Column(db.String,
                        nullable=False)
    
    
