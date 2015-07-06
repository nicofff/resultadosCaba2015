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

			#if (not error):
			#	print "Mesa " + nice_mesa + " OK"

	