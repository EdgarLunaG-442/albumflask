from back.views.usuario_views import VistaUsuario, VistasUsuarios
from back import create_app
from .models import db
from flask_restful import Api
from .views import VistaCanciones,VistaCancion,VistaAlbum,VistasAlbums


app = create_app('default')
app.app_context().push()
db.create_all()

api = Api(app)

api.add_resource(VistaCanciones,'/canciones')
api.add_resource(VistaCancion,'/cancion/<int:id_cancion>')
api.add_resource(VistasAlbums,'/albums')
api.add_resource(VistaAlbum,'/album/<int:id_album>')
api.add_resource(VistasUsuarios,'/usuarios')
api.add_resource(VistaUsuario,'/usuario/<int:id_usuario>')
