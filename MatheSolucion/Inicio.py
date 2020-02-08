from Errores import *
from variables import *
from funciones import *
import os

os.system(color_inicio)



while Inicio == True:
	try:
		os.system(borrar)
		print()
		print()
		print("   *****************************************")
		print("   *                                       *")
		print("   *         Seleccione Una Opcion         *")
		print("   *                                       *")
		print("   *****************************************")
		print()
		print(" 1 - Permutacion")
		print(" 2 - Variacion")
		print(" 3 - Combinacion")
		print(" 4 - Salir")
		seleccion = int(input(" -> "))

		if seleccion == 1:
			Permutacion()

		elif seleccion == 2:
			Variacion()

		elif seleccion == 3:
			Combinacion()

		elif seleccion == 4:
			break
		else:
			Error1()

	except ValueError:
		Error2()
