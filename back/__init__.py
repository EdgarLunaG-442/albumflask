from os import name
from flask import Flask

from .models import db

def create_app(nameApp):
	app = Flask(nameApp)
	app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///db/test.db'
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
	db.init_app(app)
	return app
