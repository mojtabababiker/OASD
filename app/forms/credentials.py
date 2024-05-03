from flask_wtf import Form, StringField, PasswordField, SubmitField, EmailField
from flask_wtf import SelectField, TextAreaField, HiddenField
from wtforms.validators import DataRequired, Email, Length, EqualTo


class LoginForm(Form):
    """
    Login form class.
    """
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
