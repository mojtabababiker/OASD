"""
model represent articals table, and handle all the work done on the
articals
"""
import os
import os.path
from models import db
from models.base_model import BaseModel


class Artical(BaseModel, db.Model):
    """
    class represent articals table, methods and oprations
    """

    __tablename__ = "articals"

    title = db.Column(db.String(32),
                    nullable=False,
                    unique=True)
    # [education, health, culture, emergancy_relief]
    section = db.Column(db.String(30),
                    nullable=False)
    content_breif = db.Column(db.String(130),
                    nullable=False)
    content = db.Column(db.Text,
                    nullable=False)
    admin_id = db.Column(db.String(60),
                    db.ForeignKey("admins.id"),
                    nullable=False)
    image_path = db.Column(db.String(72),
                    nullable=True)
    priority = db.Column(db.Integer,
                    default=0,
                    nullable=False)

    def __init__(self, title: str = None, content: str = None,
                 admin_id: str = None, image_path=None, priority=0):
        """
        initiate the artical class 
        """
        self.title = title
        self.content = content
        self.admin_id = admin_id
        self.priority = priority

        if image_path and os.path.isfile(image_path):
            dir_name = os.path.dirname(image_path)
            extension = os.path.basename(image_path).split(".")[1]
            new_path = os.path.join(dir_name, f"{self.id}.{extension}")
            os.rename(image_path, new_path)
            image_path = new_path

        self.image_path = image_path
        super().__init__()

    @property
    def date(self):
        """
        return the created_at attribute in a formatted way
        """
        return self.created_at.strftime("%d %B, %Y")

    @property
    def mdate(self):
        """
        return the updated_at attribute in a formatted way
        """
        return self.updated_at.strftime("%d %B, %Y")

    @property
    def admin(self):
        """
        return the admin instance that created this artical
        """
        from app import app  # pylint: disable=import-outside-toplevel
        from models.admins_model import Admin  # pylint: disable=import-outside-toplevel

        with app.app_context():
            admin_name = db.session.execute(
                db.select(Admin)
            ).all()

        print(admin_name)
        return admin_name
