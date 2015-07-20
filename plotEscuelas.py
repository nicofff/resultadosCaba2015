import os
from mesa import Mesa

mesas = Mesa.leer_todas(os.getcwd()+"/data")
escuelas = {}
print "comuna escuela mesa registrados votaron pro eco blanco impugnado nulo recurrido tecnico"
for mesa in mesas:

	pro=""
	eco=""
	blanco=""
	imp=""
	nul=""
	rec=""
	tec=""
	error = False
	votosListas = {}
	if mesa.get_cargada():
		votantes =mesa.get_resumen("VotantesMesa")
		votaron = mesa.get_resumen("VotantesJef")
		comuna = mesa.get_resumen("IDComuna")
		escuela = mesa.get_resumen("IDEstablecimiento")
		for listaJefe in mesa.get_listas("jefes"):
			if listaJefe["id_lista"] == "18":
				pro = str(listaJefe["votos"])
			elif listaJefe["id_lista"] == "16":
				eco = str(listaJefe["votos"])
			elif listaJefe["id_lista"] == "BLC":
				blanco = str(listaJefe["votos"])
			elif listaJefe["id_lista"] == "IMP":
				imp = str(listaJefe["votos"])
			elif listaJefe["id_lista"] == "NUL":
				nul = str(listaJefe["votos"])
			elif listaJefe["id_lista"] == "REC":
				rec = str(listaJefe["votos"])
			elif listaJefe["id_lista"] == "TEC":
				tec = str(listaJefe["votos"])

		print "%s %s %s %s %s %s %s %s %s %s %s %s" % (comuna,escuela,mesa.get_numero(),votantes,votaron,pro,eco,blanco,imp,nul,rec,tec)

