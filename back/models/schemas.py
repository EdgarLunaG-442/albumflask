from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from .cancion import Cancion
from .album import Album 
from .usuario import Usuario
from .medio import EnumDiccionario

class CancionSchema(SQLAlchemyAutoSchema):
	class Meta:
		model = Cancion
		include_relationships = True
		load_instance = True
		include_fk=True

class AlbumSchema(SQLAlchemyAutoSchema):
	medio=EnumDiccionario(attribute='medio')
	class Meta:
		model = Album
		include_relationships = True
		load_instance = True
		include_fk=True
	
class UsuarioSchema(SQLAlchemyAutoSchema):
	class Meta:
		model = Usuario
		include_relationships = True
		load_instance = True
		include_fk=True