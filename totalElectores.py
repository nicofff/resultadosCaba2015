import os
import json

for mesa in os.listdir(os.getcwd()+"/data"):
	error = False
	nice_mesa = os.path.basename(mesa)
	fullPath= os.getcwd()+"/data/"+mesa
	if os.path.getsize(fullPath) != 30:
		with open(fullPath) as fMesa:
			datosMesa = json.load(fMesa)
			totalvotantes = datosMesa["datos"]["resumen"]["VotantesMesa"]
			votantesJefeGob = datosMesa["datos"]["resumen"]["VotantesJef"]
			votantesLegislador = datosMesa["datos"]["resumen"]["VotantesLeg"]
			votantesComunero = datosMesa["datos"]["resumen"]["VotantesCom"]

			if (votantesJefeGob > totalvotantes or votantesLegislador > totalvotantes or votantesComunero > totalvotantes):
				print "Mas votos que votantes en mesa " + nice_mesa
				error = True

			if (votantesJefeGob != votantesLegislador or votantesJefeGob != votantesComunero):
				print "Diferencia de votos entre categorias " + nice_mesa
				error = True

			### Total Jefe de Gobierno
			totalJefe = 0
			for listaJefe in datosMesa["datos"]["jefes"]["listas"]:
				totalJefe += listaJefe["votos"]

			if totalJefe != votantesJefeGob:
				print "Diferencia en total Jefe de Gobierno. Mesa "+ nice_mesa
				error=True


			### Total Legisladores
			totalLegislador = 0
			for listaLegislador in datosMesa["datos"]["legisladores"]["listas"]:
				totalLegislador += listaLegislador["votos"]

			if totalLegislador != votantesLegislador:
				print "Diferencia en total legisladores. Mesa "+ nice_mesa
				error=True

			### Total Comuneros
			totalComunero = 0
			for listaComuneros in datosMesa["datos"]["comuneros"]["listas"]:
				totalComunero += listaComuneros["votos"]

			if totalComunero != votantesComunero:
				print "Diferencia en total comuneros. Mesa "+ nice_mesa
				error=True

			#if (not error):
			#	print "Mesa " + nice_mesa + " OK"

	