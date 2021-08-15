from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from .dbinstance import db
from .album_cancion import canciones_albumes

class Cancion(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	titulo = db.Column(db.String(128))
	minutos = db.Column(db.Integer)
	segundos = db.Column(db.Integer)
	interprete = db.Column(db.String(128))
	albumes = db.relationship('Album',secondary=canciones_albumes,back_populates='canciones')

