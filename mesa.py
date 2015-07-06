import json
import os

class Mesa:

	def __init__(self,path):
		with open(path) as fMesa:
			self.data = json.load(fMesa)

			if not (type(self.data["datos"]) is dict):
				self.cargada = False
			else:
				self.cargada = True
				self.numero = self.data["datos"]["resumen"]["Descripcion"]

	def get_resumen(self,key):
		return self.data["datos"]["resumen"][key]

	def get_listas(self,categoria):
		return self.data["datos"][categoria]["listas"]

	def get_numero(self):
		return self.numero

	def get_cargada(self):
		return self.cargada

	@classmethod
	def leer_todas(cls,path):		
		mesas = []
		for file_mesa in os.listdir(path):
			fullPath = os.path.join(path,file_mesa)
			mesas.append(cls(fullPath))

		return mesas

