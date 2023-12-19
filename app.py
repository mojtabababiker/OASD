from flask import Flask, render_template
from models import db
from models.admins_model import Admin
from models.articals_model import Artical
from models.job_offers_model import JobOffer

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = db.url
# configure the extension app for the database connection
db.init_app(app=app)
db.create_tables()
