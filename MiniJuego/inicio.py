from variables_constantes import *
from funciones import *
from modos_de_juego import *
from errores import *
import os
import time

"""
Borrar(limpiar)
Color(purpura)
print()
print("    Bienvenidos")
Tiempo(tiempo)
Borrar(limpiar)

Cargando(limpiar)
"""

while inicio == True:
	try:
		Color(purpura)
		Borrar(limpiar)
		print()
		print("   ***************************************")
		print("   *                                     *")
		print("   *         Elija Modo de Juego         *")
		print("   *                                     *")
		print("   ***************************************")
		print()
		print(" 1 - Adivinador de Numero")
		print(" 2 - Dado")
		print(" 3 - Dos Dados")
		print(" 4 - Salir")
		print()
		seleccion = int(input(" -> "))

		if seleccion == 1:
			Modos_de_Juego.Modo1()
			Borrar(limpiar)
		elif seleccion == 2:
			Modos_de_Juego.Modo2()
			Borrar(limpiar)
		elif seleccion == 3:
			Modos_de_Juego.Modo3()
			Borrar(limpiar)
		elif seleccion == 4:
			inicio = False
			Borrar(limpiar)
			break
		else:
			Errores.Error1()

	except ValueError:
		Errores.Error2()


Color(rojo)
