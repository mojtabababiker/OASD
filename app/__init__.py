"""
This module initializes the Flask application and configures all the necessary extensions.
"""
import secrets
from flask import Flask, Response  # pylint: disable=import-error
from flask_wtf.csrf import CSRFProtect
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from models import db
from models.admins_model import Admin

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = db.url
# generate a random secret key used for session management
app.secret_key = secrets.token_urlsafe(16)
csrf = CSRFProtect(app)  #  configure the app to use CSRF forms protection
# configure the app to use bcrypt for password hashing and verification
bcrypt = Bcrypt(app)
# configure the app to use flask login manager for user authentication
login_manager = LoginManager(app)
# configure the extension app for the database connection
db.init_app(app=app)
db.create_tables()  # create all database tables if they do not exist

@app.teardown_appcontext
def shutdown_session(exception=None):
    """
    Close the database session after the request is finished.
    """
    if not exception:
        db.session.remove()
    else:
        pass

@login_manager.user_loader
def load_user(user_id: str) -> Admin:
    """
    login manager user loader function to load the user from the database with the user_id
    """
    return db.session.execute(db.select(Admin).filter_by(id=user_id)).scalar()

def unauth_callback() -> Response:
    """
    the unauthorized call back  function to handle the redirection and flushing
    messages to view
    """
    return admin_page("Login required")

# called when a user tries to access a protected route without being authenticated
login_manager.unauthorized_handler(unauth_callback)

from app.views.admin_views import *  # pylint: disable=wrong-import-position
from app.views.general_views import *  # pylint: disable=wrong-import-position
