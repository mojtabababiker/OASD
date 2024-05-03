#!/usr/bin/env python
"""
This module contains the forms for the credentials [login, register, etc.].
"""
from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileRequired
from wtforms import StringField, PasswordField
from wtforms import SubmitField, FileField
from wtforms.validators import DataRequired, Length, EqualTo, Email, ValidationError
from app import app, db
from models.admins_model import Admin

class LoginForm(FlaskForm):
    """
    Login form class.
    """
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


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
            raise ValidationError('Last name alrady exists')

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
                                FileAllowed(['jpg', 'png', 'jpeg', 'raw'])
                            ])
