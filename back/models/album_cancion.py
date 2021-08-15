from .dbinstance import db

canciones_albumes = db.Table('canciones_albumes',db.metadata,
    db.Column('cancion_id', db.Integer, db.ForeignKey('cancion.id'), primary_key=True),
    db.Column('album_id', db.Integer, db.ForeignKey('album.id'), primary_key=True)
)