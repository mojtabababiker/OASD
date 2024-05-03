from flask import Flask  # pylint: disable=import-error
from models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = db.url
# configure the extension app for the database connection
db.init_app(app=app)
db.create_tables()

@app.teardown_appcontext
def shutdown_session(exception=None):
    """
    Close the database session after the request is finished.
    """
    if not exception:
        db.session.remove()
    else:
        pass

from app.views.admin_views import *  # pylint: disable=wrong-import-position
from app.views.general_views import *  # pylint: disable=wrong-import-position
