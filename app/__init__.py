from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from .momentjs import momentjs

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
app.jinja_env.globals['momentjs'] = momentjs


from app import views, models
