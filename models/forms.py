"""
Admin login form module
"""
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, IntegerField
from wtforms import SubmitField, TextAreaField, FileField
from wtforms.validators import DataRequired, Length, EqualTo, Email, ValidationError
from flask_wtf.file import FileAllowed, FileRequired
from flask_login import current_user, login_required
from models import db, app
from models.admins_model import Admin


class LoginForm(FlaskForm):
    """
    a login form class for application admin dashboard
    """

    email_address = StringField(label="Email Address", validators=[DataRequired(), Email()])
    password = PasswordField(label="Passowrd", validators=[DataRequired(),
                                                            Length(min=12)])
    submit = SubmitField(label="Login")


class AddAdminForm(LoginForm):
    """
    register a new admin form
    """
    def validate_last_name(self, name):
        """
        Check if the enterd Admin first name is already in use
        """
        with app.app_context():
            admin = db.session.execute(
                db.select(Admin).filter_by(last_name=name.data)
                ).first()
        if admin:
            raise ValidationError('First name alrady exists')

    def validate_email_address(self, email):
        """
        check if the email adress already in used with anther user
        """
        with app.app_context():
            admin = db.session.execute(
                db.select(Admin).filter_by(email=email.data)
            ).first()
        if admin:
            raise ValidationError('Email Address is in used')

    first_name = StringField(label="First Name:", 
                             validators=[DataRequired(),
                            Length(min=3, max=32)]
                            )
    last_name = StringField(label="Last Name:", 
                             validators=[DataRequired(),
                            Length(min=3, max=32)]
                            )
    confirm_password = PasswordField(label="Confirm Password:",
                                     validators=[DataRequired(),
                                     EqualTo('password')]
                            )
    phone_num = StringField(label="Phone Number")
    facebook_account = StringField(label='FaceBook Account')
    insta_account = StringField(label='Instagram Account')
    x_account = StringField(label='X Accounte')
    profile_img = FileField(label="Load Image",
                        validators=[
                            FileRequired(),
                            FileAllowed(['jpg', 'png', 'jpeg', 'raw'])]
                            )


class EditProfileForm(FlaskForm):
    """
    register a new admin form
    """
    first_name = StringField(label="First Name:", 
                            validators=[Length(min=3, max=32)],
                            
                            )
    last_name = StringField(label="Last Name:", 
                            validators=[Length(min=3, max=32)],
                            
                            )
    email_address = StringField(label="Email Address", validators=[DataRequired(), Email()])
    password = StringField(label="New Password:",
                            validators=[Length(min=12)],
                            )
    confirm_password = StringField(label="Confirm Password:",
                            validators=[EqualTo('password')],
                            )
    phone_num = StringField(label="Phone Number")
    facebook_account = StringField(label='FaceBook Account')
    insta_account = StringField(label='Instagram Account')
    x_account = StringField(label='X Accounte') 
    profile_img = FileField(label="Load Image",
                            validators=[FileAllowed(['jpg', 'png', 'jpeg', 'raw'])]
                            )
    submit = SubmitField(label="Save Changes")


class AddArticelForm(FlaskForm):
    """
    form for adding article to the blog
    """
    def validate_title(self, title):
        """
        if the title is used on anther article
        """
        from models.articals_model import Artical

        with app.app_context():
            article = db.session.execute(
                db.select(Artical).filter_by(title=title.data, section=self.section.data)
            ).first()
        if article:
            print('=========TITLE IS USED================')
            raise ValidationError('Title is used and not valide')
    # set the allowed file type to bw uploaded (images only)

    title = StringField(label="Title", validators=[DataRequired(), Length(min=6, max=32)])
    content_breif = TextAreaField(label="Content Brief", validators=[Length(min=32, max=128)])
    content = TextAreaField(label="Text", description="Article Content",
                             validators=[DataRequired()])
    section = SelectField(label="Section", 
                          choices=["Education", "Health",
                                    "Culture", "Em-Relies"],
                          default="Education",
                          validators=[DataRequired()])
    priority = IntegerField(label="Priority", default=0)
    image = FileField(label="Load Image",
                        validators=[
                            FileRequired(),
                            FileAllowed(['jpg', 'png', 'jpeg', 'raw'])
            ])
    submit = SubmitField("Save")