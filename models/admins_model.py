"""
model for the application admins class
"""
import os
import os.path
from werkzeug.utils import secure_filename
from models import db
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
                    unique=True)
    password_hashed = db.Column(db.String(72),
                    nullable=False,
                    unique=False)
    profile_img = db.Column(db.String(72),
                    nullable=False,
                    unique=True,
                    default='default.png')
    acount_insta = db.Column(db.String(72), nullable=True)
    acount_fb = db.Column(db.String(72), nullable=True)
    acount_x = db.Column(db.String(72), nullable=True)
    phone_num = db.Column(db.String(72), nullable=True)
    articals = db.relationship("Artical", backref="admin",
                    cascade="all, delete-orphan")
    job_offers = db.relationship("JobOffer", backref="admin",
                    cascade="all, delete-orphan")

    def __init__(self, first_name: str = '', last_name: str = '',
                 email: str = '', password = ''):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        # self.password_hashed = bcrypt.generate_password_hash(password).decode('utf-8')
        super().__init__()

    def update(self, form):
        """
        update the admin attributes from the form data
        """
        not_attr = ['csrf_token', 'submit', 'confirm_password']
        for field in form:
            if field.data and field.name not in not_attr:
                if (field.name == 'profile_img'):
                    self.profile = field.data
                else :
                    setattr(self, field.name, field.data)
                    print(f"==========> {field.name} {field.data}")

    def check_password(self, password: str) -> bool:
        """
        check password hash with the given password
        """
        from app import bcrypt  # pylint: disable=import-outside-toplevel

        return bcrypt.check_password_hash(self.password_hashed, password)

    @property
    def password(self):
        """
        password property setter
        """
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password: str):
        """
        password property setter
        """
        from app import bcrypt  # pylint: disable=import-outside-toplevel

        self.password_hashed = bcrypt.generate_password_hash(password).decode('utf-8')

    @property
    def profile(self):
        """
        profile_img property getter
        """
        return self.profile_img

    @profile.setter
    def profile(self, img):
        """
        profile_img property setter
        """
        from app import app  # pylint: disable=import-outside-toplevel

        image_path = secure_filename(img.filename)
        if image_path:
            dir_name = os.path.dirname(app.instance_path)
            extension = os.path.basename(image_path).split(".")[1]
            new_path = os.path.join(dir_name, 'app', 'static', 'images', 'admin',
                                    f"{self.id}.{extension}")
            try:
                os.remove(new_path)
            except Exception:  # pylint: disable=broad-except
                pass
            img.save(new_path)
            image_path = f"{self.id}.{extension}"
            print(image_path)
        else:
            # if no image was provided
            image_path = "default.png"
        self.profile_img = image_path

    # login manager methods
    def is_authenticated(self):
        """
        check if the user is authenticated
        """
        return True

    def is_active(self):
        """
        check if the user is active
        """
        return True

    def is_anonymous(self):
        """
        check if the user is anonymous
        """
        return False

    def get_id(self):
        """
        get the user id
        """
        return self.id
