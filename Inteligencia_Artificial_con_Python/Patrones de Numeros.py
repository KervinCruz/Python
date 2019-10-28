"""
	Inteligencia Artificial: Patrones

	En esta ocacion desarrolle un algoritmo que permite a travez de dos
	variables de entrada descifrar el patròn que estàn siguiendo los numeros
	ingresados. Ejemplo:

	Entrada: 05, Salida: 10
	Entrada: 20, Salida: 40
	Entrada: 25, Salida: 50

	Cuando digitemos la entrada, pero no pongamos la salida, el programa a travèz
	de lo que ha aprendido sabrà cual es el patròn que estàs siguiendo, en este caso
	el de multiplicar por dos la entrada. Ejemplo:

	Entrada: 50, Salida: ? = 100

"""



import os

salida = " "; vuelta = 1 

while True:
	os.system("cls")
	entrada = int(input("-> Introduce Entrada: "))

	if entrada == 11052000:
		os.system("cls")
		break

	salida = input("-> Introduce Salida: ")


	if vuelta == 1:
		valor1 = entrada

		if salida != "":
			valor2 = int(salida)
			vuelta = 2

		else: 
			if valor3 <= valor4:
				diferencia = valor4 - valor3
			else:
				diferencia = valor3 - valor4

			if diferencia == ((valor3 * 2)/2):
				valor2 = str(valor1*2)

			else:
				valor2 = str(valor1+diferencia)

			os.system("cls")
			print("-> Introduce Entrada: ", valor1)
			print("-> Introduce Salida: ", valor2)
			input()

	elif vuelta == 2:
		valor3 = entrada

		if salida != "":
			valor4 = int(salida)
			vuelta = 1
		else: 
			if valor1 <= valor2:
				diferencia = valor2 - valor1
			else:
				diferencia = valor1 - valor2

			if diferencia == ((valor1 * 2)/2):
				valor4 = str(valor3*2)

			else:
				valor4 = str(valor3+diferencia)

			os.system("cls")
			print("-> Introduce Entrada: ", valor3)
			print("-> Introduce Salida: ", valor4)
			input()
