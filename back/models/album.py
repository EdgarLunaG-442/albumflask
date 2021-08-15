from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from .medio import  Medio
from .dbinstance import db
from .album_cancion import canciones_albumes



class Album(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	titulo = db.Column(db.String(128))
	anio = db.Column(db.Integer)
	descripcion = db.Column(db.String(128))
	medio = db.Column(db.Enum(Medio))
	canciones = db.relationship('Cancion',secondary=canciones_albumes,back_populates='albumes')
	usuarioid = db.Column(db.Integer, db.ForeignKey('usuario.id'))
	__table_args__ = tuple(db.UniqueConstraint('usuario','titulo',name='titulo_unico_album'))


