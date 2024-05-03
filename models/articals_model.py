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

    title = db.Column(db.String(60),
                    nullable=False,
                    unique=True)
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
