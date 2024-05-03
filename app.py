from models import login_manager
from models import db
from models import app
from models.routes import *

@login_manager.user_loader
def load_user(user_id):
    from models.admins_model import Admin
    return db.session.execute(db.select(Admin).filter_by(id=user_id)).scalar()

def unauth_callback():
    """
    the unauthorized call back  function to handle the redirection and flushing
    messages to view
    """
    return admin_page("Login required")

login_manager.unauthorized_handler(unauth_callback)

if __name__ == '__main__':
    app.run('127.0.0.1', 5500, debug=True)