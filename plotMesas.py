import os
from mesa import Mesa

mesas = Mesa.leer_todas(os.getcwd()+"/data")

for mesa in mesas:
	pro=""
	eco=""
	fpv=""
	ayl=""
	fit=""
	error = False
	votosListas = {}
	if mesa.get_cargada():
		for listaJefe in mesa.get_listas("jefes"):
			if listaJefe["id_lista"] == "18":
				pro = str(listaJefe["pct_valido"])
			elif listaJefe["id_lista"] == "16":
				eco = str(listaJefe["pct_valido"])
			elif listaJefe["id_lista"] == "23":
				fpv = str(listaJefe["pct_valido"])
			elif listaJefe["id_lista"] == "81":
				ayl = str(listaJefe["pct_valido"])
			elif listaJefe["id_lista"] == "17":
				fit = str(listaJefe["pct_valido"])

		print "%s %s %s %s %s %s" % (mesa.get_numero(),pro,eco,fpv,ayl,fit)

