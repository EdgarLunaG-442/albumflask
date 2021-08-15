
from back.models import album
from flask_restful import Resource
from flask import request
from ..models import Album,db,Cancion,Medio
from ..helpers import serializarAlbum,serializarAlbumes


class VistasAlbums(Resource):
	def get(self):
		return serializarAlbumes()
		
	def post(self):
		nuevoAlbum = Album(
			titulo = request.json['titulo'],
			anio = request.json['anio'],
			descripcion = request.json['descripcion'],
			medio = request.json['medio']
		)
		db.session.add(nuevoAlbum)
		db.session.commit()
		return serializarAlbum(nuevoAlbum)

class VistaAlbum(Resource):
	def put(self,id_album):
		albumQuery = Album.query.get_or_404(id_album)
		albumQuery.titulo = request.json.get('titulo',albumQuery.titulo)
		albumQuery.anio = request.json.get('anio',albumQuery.anio)
		albumQuery.descripcion = request.json.get('descripcion',albumQuery.descripcion )
		if request.json.get('medio',None):
			if request.json['medio'] in Medio._value2member_map_:
				albumQuery.medio = request.json.get('medio',albumQuery.medio)
			else:
				return {"message":"El medio no es valido"},404
		if request.json.get('id_cancion_agregar',None):
			cancionAgregar = Cancion.query.get_or_404(request.json['id_cancion_agregar'])
			albumQuery.canciones.append(cancionAgregar)
		if request.json.get('id_cancion_eliminar',None):
			cancionRetirar = Cancion.query.get_or_404(request.json['id_cancion_eliminar'])
			albumQuery.canciones.remove(cancionRetirar)
		db.session.commit()
		return serializarAlbum(albumQuery)

	def get(self,id_album):
		albumQuery = Album.query.get_or_404(id_album)
		return serializarAlbum(albumQuery)

	def delete(self,id_album):
		albumQuery = Album.query.get_or_404(id_album)
		db.session.delete(albumQuery)
		db.session.commit()
		return {"message":"Se elimino correctamente"}
