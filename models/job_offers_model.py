"""
model represent the jobs_offer table, and handle all the oprations
on it
"""

from models import db
from models.base_model import BaseModel


class JobOffer(BaseModel, db.Model):
    """
    class that represetn the jobs offers, and defines its database
    table
    """
    __table__ = "job_offers"

    job_title = db.Column(db.String(60),
                    nullable=False,
                    unique=True)
    content = db.Column(db.Text,
                    nullable=False)
    admin_id = db.Column(db.String(60),
                    db.ForeignKey("admins.id"),
                    nullable=False)
    def __init__(self, title, content, admin_id):
        self.job_title = title
        self.content = content
        self.admin_id = admin_id
        super().__init__()