from variables import *


def Porciento():
	os.system(borrar)
	numero = int(input("\n\n\n   -> Ingrese el valor a calcular el porcentage: "))
	valor = int(input("   -> Ingrese el Porcentage: "))

	resultado = numero * (valor / 100)
	print(resultado)
	input()