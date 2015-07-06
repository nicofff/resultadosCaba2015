import os
from mesa import Mesa

mesas = Mesa.leer_todas(os.getcwd()+"/data")
escrutadas = 0
noEscrutadas = 0
for mesa in mesas:
	if mesa.get_cargada():
		escrutadas +=1
	else:
		noEscrutadas +=1


print "escrutadas: " + str(escrutadas)
print "No escrutadas: " + str(noEscrutadas)