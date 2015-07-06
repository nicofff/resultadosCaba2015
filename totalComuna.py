import os
from mesa import Mesa
import pprint

mesas = Mesa.leer_todas(os.getcwd()+"/data")

comunas = {}
for mesa in mesas:
	if mesa.get_cargada():
		comuna = mesa.get_resumen("IDComuna")
		if not comuna in comunas:
			comunas[comuna] = {}
			comunas[comuna]["jefe"] = {}

		for listaJefe in mesa.get_listas("jefes"):
			lista = listaJefe["lista"] 
			if not lista in comunas[comuna]["jefe"]:
				comunas[comuna]["jefe"][lista]= listaJefe["votos"]
			else:
				comunas[comuna]["jefe"][lista] += listaJefe["votos"]
		
		if not "votaron" in comunas[comuna]:
			comunas[comuna]["votaron"] = mesa.get_resumen("VotantesJef")
			comunas[comuna]["en padron"] = mesa.get_resumen("VotantesMesa")
		else:
			comunas[comuna]["votaron"] += mesa.get_resumen("VotantesJef")
			comunas[comuna]["en padron"] += mesa.get_resumen("VotantesMesa")


pp = pprint.PrettyPrinter(indent=4)
pp.pprint(comunas)

total = {}
for icomuna in comunas:
	comuna = comunas[icomuna]
	for lista in comuna["jefe"]:
		if not lista in total:
			total[lista] = comuna["jefe"][lista]
		else:
			total[lista] += comuna["jefe"][lista]


	if not "votaron" in total:
		total["votaron"] = comuna["votaron"]
		total["en padron"] = comuna["en padron"]
	else:
		total["votaron"] += comuna["votaron"]
		total["en padron"] += comuna["en padron"]


pp.pprint(total)