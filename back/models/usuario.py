from .dbinstance import db
from .album import Album



class Usuario(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	nombre = db.Column(db.String(128))
	contrasena = db.Column(db.String(128))
	albumes = db.relationship('Album', backref='usuario' ,lazy=True, cascade="all, delete-orphan")