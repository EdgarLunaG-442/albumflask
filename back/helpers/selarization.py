from ..models import Cancion,CancionSchema,Album,AlbumSchema,Usuario,UsuarioSchema
cancion_schema = CancionSchema()
album_schema = AlbumSchema()
usuario_schema = UsuarioSchema()
def seliarizarCanciones():
	return [cancion_schema.dump(cancion) for cancion in Cancion.query.all()]
def serializarCancion(cancion):
	return cancion_schema.dump(cancion)
def serializarAlbumes():
	return [album_schema.dump(album) for album in Album.query.all()]
def serializarAlbum(album):
	return album_schema.dump(album)
def serializarUsuarios():
	return [usuario_schema.dump(usuario) for usuario in Usuario.query.all()]
def serializarUsuario(usuario):
	return usuario_schema.dump(usuario)
