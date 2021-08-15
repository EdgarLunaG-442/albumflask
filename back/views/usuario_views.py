
from flask_restful import Resource
from flask import request
from ..models import Album,db,Usuario,UsuarioSchema
from ..helpers import serializarUsuario,serializarUsuarios
usuario_schema = UsuarioSchema()

class VistasUsuarios(Resource):
	def get(self):
		return serializarUsuarios()
		
	def post(self):
		nuevoUsuario= Usuario(
			nombre = request.json['nombre'],
			contrasena = request.json['contrasena']
		)
		db.session.add(nuevoUsuario)
		db.session.commit()
		return serializarUsuario(nuevoUsuario)

class VistaUsuario(Resource):
	def put(self,id_usuario):
		usuarioQuery = Usuario.query.get_or_404(id_usuario)
		usuarioQuery.nombre = request.json.get('nombre',usuarioQuery.nombre)
		usuarioQuery.contrasena = request.json.get('contrasena',usuarioQuery.contrasena)
		if request.json.get('id_album_agregar',None):
			albumQuery = Album.query.get_or_404(request.json['id_album_agregar'])
			usuarioQuery.albumes.append(albumQuery)
		if request.json.get('id_album_eliminar',None):
			albumQuery = Album.query.get_or_404(request.json['id_album_eliminar'])
			usuarioQuery.albumes.remove(albumQuery)
		db.session.commit()
		return serializarUsuario(usuarioQuery)

	def get(self,id_usuario):
		usuarioQuery = Usuario.query.get_or_404(id_usuario)
		return serializarUsuario(usuarioQuery)

	def delete(self,id_usuario):
		UsuarioQuery = Usuario.query.get_or_404(id_usuario)
		db.session.delete(UsuarioQuery)
		db.session.commit()
		return {"message":"Se elimino correctamente"}
