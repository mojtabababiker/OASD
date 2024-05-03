from models.engine.db_storage import DBStorage
import secrets
from flask import Flask
from flask_wtf.csrf import CSRFProtect
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.secret_key = secrets.token_urlsafe(16)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///app.db"
# f"mysql://{db.db_user}:{db.db_psswd}@{db.db_host}:3306/{db.db_name}"

csrf = CSRFProtect(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
db = DBStorage()
db.init_app(app)


# db.create_tables(app)
