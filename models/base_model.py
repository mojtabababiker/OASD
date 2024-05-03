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

    def __init__(self, *args, **kwargs):
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
        from models import app
        with app.app_context():
            db.session.add(self)
            db.session.commit()

    def delete(self):
        """
        delete the record from the session and commit the change
        """
        from models import app
        with app.app_context():
            db.session.delete(self)
            db.session.commit()

    def parse(self):
        """
        Convert the content of the instance from markdown to html and return the result
        """
        import markdown
        import os
        import os.path

        if hasattr(self, 'content'):
            html = markdown.markdown(self.content)
            with open(f'models/templates/{self.id}.html', mode='w', encoding='utf-8') as f:
                print(f"{self.id}.html")
                f.write(html)
            return f"{self.id}.html"
        
    def __repr__(self):
        """
        Costumize the magic method __str__
        """
        _str = f"id: {self.id}\nTitle: {self.title}\nContent: {self.parse()}\n"
        _str += f"Create at: {self.created_at}\nUpdate at: {self.updated_at}"
        return _str
        

    # def to_dict(self):
    #     """
    #     create and return costumize dictionry of the instance
    #     """
        