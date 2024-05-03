"""
model for the application admins class
"""
import os.path
from models import db, bcrypt
from models.base_model import BaseModel
from models.articals_model import Artical
from models.job_offers_model import JobOffer
from sqlalchemy.orm import aliased
from flask_login import UserMixin
from werkzeug.utils import secure_filename


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

    def __init__(self):
        BaseModel.__init__(self)

    def __repr__(self):
        _str = f"id: {self.id}\nFirst Name: {self.first_name}"
        return _str

    @property
    def password(self):
        """
        return the hashed encryptred Admin password
        """
        return self.password_hashed

    @password.setter
    def password(self, plain_passwd):
        """
        set the value of password after hash the plain_passwd
        """
        self.password_hashed = bcrypt.generate_password_hash(
                                plain_passwd
                                ).decode('utf-8')

    @property
    def is_active(self):
        return True

    @property
    def is_authenticated(self):
        return self.is_active

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)
 
    def check_password(self, passwd):
        """
        validate the user inputed password
        """
        return bcrypt.check_password_hash(self.password, passwd)

    def update(self, form):
        """
        update the admin instance with all the data in the form
        the form is came from the route, which enterd by the user
        either in the creation of the admin or editing the profile
        """
        from models import app
        self.first_name = form.first_name.data
        self.last_name = form.last_name.data
        self.email = form.email_address.data
        if form.password.data != self.password:
            self.password = form.password.data
        self.phone_num = form.phone_num.data
        self.acount_fb = form.facebook_account.data
        self.acount_insta = form.insta_account.data
        self.acount_x = form.x_account.data

        
        img = form.profile_img.data
        image_path = secure_filename(img.filename)
        if image_path:
            dir_name = os.path.dirname(app.instance_path)
            extension = os.path.basename(image_path).split(".")[1]
            new_path = os.path.join(dir_name, 'models', 'static', 'admin', 'images',
                                    f"{self.id}.{extension}")
            try:
                os.remove(new_path)
            except Exception:
                pass
            img.save(new_path)
            image_path = f"{self.id}.{extension}"
            print(image_path)
        else:
            # if no image was provided
            image_path = "default.png"
        self.profile_img = image_path