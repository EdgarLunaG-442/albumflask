import enum
from marshmallow import fields

class Medio(enum.Enum):
	DISCO="DISCO"
	CASETE="CASETE"
	CD="CD"
	
class EnumDiccionario(fields.Field):
	def _serialize(self, value, attr: str, obj, **kwargs):
		if value is None:
			return None
		return {'key':value.name,'value':value.value}
