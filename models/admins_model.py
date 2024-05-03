"""
model for the application admins class
"""
from uuid import UUID
from sqlalchemy.orm import aliased  # pylint: disable=import-error
import os.path
from models import db, bcrypt
from models.base_model import BaseModel
from models.articals_model import Artical  # pylint: disable=unused-import
from models.job_offers_model import JobOffer  # pylint: disable=unused-import


class Admin(BaseModel, db.Model):
    """
    application admins class which represent the admins table
    and handle all the oprations on the admin process
    """
    __tablename__ = "admins"
    first_name = db.Column(db.String(30),
                    nullable=False,
                    unique=True)
    last_name = db.Column(db.String(30),
                    nullable=False,
                    unique=False)
    email = db.Column(db.String(30),
                    nullable=False,
                    primary_key=True)
    password_hashed = db.Column(db.String(30),
                    nullable=False,
                    unique=False)
    profile_img = db.Column(db.String,
                    nullable=False,
                    unique=True,
                    default='default.png')
    acount_insta = db.Column(db.String, nullable=True)
    acount_fb = db.Column(db.String, nullable=True)
    acount_x = db.Column(db.String, nullable=True)
    phone_num = db.Column(db.String, nullable=True)
    articals = db.relationship("Artical", backref="admin",
                    cascade="all, delete-orphan")
    job_offers = db.relationship("JobOffer", backref="admin",
                    cascade="all, delete-orphan")

    def __init__(self, first_name: str = '', last_name: str = '',
                 email: str = '', password: UUID = ''):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        super().__init__()


aliased_admins = aliased(Admin, "admin")
