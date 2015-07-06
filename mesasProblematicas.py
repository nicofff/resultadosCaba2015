import os
from mesa import Mesa

mesas = Mesa.leer_todas(os.getcwd()+"/data")

for mesa in mesas:
	if mesa.get_cargada():
		for listaJefe in mesa.get_listas("jefes"):
			if (listaJefe["id_candidato"] == None and listaJefe["id_lista"] != "BLC" and listaJefe["pct_total"] > 3):
				print "Mesa " + mesa.get_numero() + " con problemas"