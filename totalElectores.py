import os
from mesa import Mesa

mesas = Mesa.leer_todas(os.getcwd()+"/data")

for mesa in mesas:
	error = False

	if mesa.get_cargada():
		totalvotantes = mesa.get_resumen("VotantesMesa")
		electores = mesa.get_resumen("Electores")
		votantesJefeGob = mesa.get_resumen("VotantesJef")
		#votantesLegislador = mesa.get_resumen("VotantesLeg")
		#votantesComunero = mesa.get_resumen("VotantesCom")

		if (totalvotantes != electores):
			print "Electores != Votantes. Mesa: " + mesa.numero
			error = True

		if (votantesJefeGob > totalvotantes):
			print "Mas votos que votantes en mesa " + mesa.numero
			error = True

		#if (votantesJefeGob != votantesLegislador or votantesJefeGob != votantesComunero):
		#	print "Diferencia de votos entre categorias " + mesa.numero
		#	error = True

		### Total Jefe de Gobierno
		totalJefe = 0
		for listaJefe in mesa.get_listas("jefes"):
			totalJefe += listaJefe["votos"]

		if totalJefe != votantesJefeGob:
			print "Diferencia en total Jefe de Gobierno. Mesa "+ mesa.numero
			error=True

		#if (not error):
		#	print "Mesa " + mesa.numero + " OK"

	