from Errores import *
from variables import *
import os
import time

def Variacion():
	while True:
		while True:
			try:
				os.system(borrar)
				print()
				print()
				print("   ***************************************")
				print("   *                                     *")
				print("   *              Variacion              *")
				print("   *                                     *")
				print("   ***************************************")
				print()
				m = int(input(" Ingrese el valor de M: "))	
				n = int(input(" Ingrese el valor de N: "))
				break
			except ValueError:
				Error2()


		divisor = m-n
		factorialM = m
		factorialDivisor = divisor
		
		#Mostrar Proceso
		convercionM = str(m)
		convercionN = str(n)
		convercionDivisor = str(divisor)
		proceso_M = convercionM
		proceso_divisor = str(divisor)

		parte1 = "   -> V = " + convercionM + "! / " + "(" + convercionM + "-" + convercionN + ")!"
		parte2 = "   -> V = " + convercionM + "! / " + convercionDivisor + "!"

		# Factorizando M
		sumando = 0
		while factorialM > 1:
			sumando += 1
			proceso_M += "("+ convercionM +"-"+str(sumando)+")"
			factorialM -= 1
			m *= factorialM

		# Factorizando M-N
		sumando = 0
		while factorialDivisor > 1:
			sumando += 1
			proceso_divisor += "("+ convercionDivisor +"-"+str(sumando)+")"
			factorialDivisor -=1
			divisor *= factorialDivisor

		parte3 = "   -> V = " + proceso_M + " / " + proceso_divisor
		parte4 = "   -> V = " + str(m) + " / " + str(divisor)

		resultado = m/divisor

		parte5 = "   -> V = " + str(resultado)		

		while True:
			try:
				os.system(borrar)
				print()
				print()
				print("   ***************************************")
				print("   *                                     *")
				print("   *              Variacion              *")
				print("   *                                     *")
				print("   ***************************************")
				print()
				print("         Formula Lineal: V = m!/(m-n)!")
				print()
				print(" Proceso Logico:           Datos: m = " + convercionM + "   n = " + convercionN)
				print()

				#Imprimiendo el Proceso
				print(parte1)
				time.sleep(tiempo_espera)
				print(parte2)
				time.sleep(tiempo_espera)
				print(parte3)
				time.sleep(tiempo_espera)
				print(parte4)
				time.sleep(tiempo_espera)
				print(parte5)
				time.sleep(tiempo_espera)

				print()
				print(" El resultado para la Variacion es: ",resultado)
				print()
				print("--------------------------------------------------------------")
				print()
				print(" Seleccione una Opcion")
				print()
				print(" 1 - Otra Operación")
				print(" 2 - Volver al Menu")
				seleccion = int(input(" ->"))

				if seleccion == 1:
					break
				elif seleccion == 2:
					break
				else:
					Error1()
			
			except ValueError:
				Error2()

		if seleccion == 2:
			break


def Permutacion():
	while True:
		while True:
			try:
				os.system(borrar)
				print()
				print()
				print("   ***************************************")
				print("   *                                     *")
				print("   *             Permutacion             *")
				print("   *                                     *")
				print("   ***************************************")
				print()	
				n = int(input(" Ingrese el valor de N: "))
				break
			except ValueError:
				Error2()


		factorialN = n
		
		# Para mostrar proceso
		sumando = 0
		mostrar = str(n)
		proceso = mostrar

		# Factorizando N
		while factorialN > 1:
			sumando += 1
			proceso += "("+ mostrar +"-"+str(sumando)+")"
			factorialN -= 1
			n *= factorialN

		while True:
			try:
				os.system(borrar)
				print()
				print()
				print("   ***************************************")
				print("   *                                     *")
				print("   *             Permutacion             *")
				print("   *                                     *")
				print("   ***************************************")
				print()
				print("            Formula Lineal: Pn = n!")
				print()
				print(" Proceso Logico: " + proceso)
				print()
				print(" El resultado para la Variacion es: ",n)
				print()
				print("--------------------------------------------------------------")
				print()
				print(" Seleccione una Opcion")
				print()
				print(" 1 - Otra Operación")
				print(" 2 - Volver al Menu")
				seleccion = int(input(" ->"))

				if seleccion == 1:
					break
				elif seleccion == 2:
					break
				else:
					Error1()
			
			except ValueError:
				Error2()

		if seleccion == 2:
			break


def Combinacion():
	while True:
		while True:
			try:
				os.system(borrar)
				print()
				print()
				print("   ***************************************")
				print("   *                                     *")
				print("   *             Combinacion             *")
				print("   *                                     *")
				print("   ***************************************")
				print()
				m = int(input(" Ingrese el valor de M: "))	
				n = int(input(" Ingrese el valor de N: "))
				break
			except ValueError:
				Error2()


		divisor = m-n
		factorialN = n
		factorialM = m
		factorialDivisor = divisor
		
		#Mostrar Proceso
		convercionM = str(m)
		convercionN = str(n)
		convercionDivisor = str(divisor)
		proceso_N = convercionN
		proceso_M = convercionM
		proceso_divisor = str(divisor)

		parte1 = "   -> C = " + convercionM + "! / " + convercionN + "! * (" + convercionM + "-" + convercionN + ")!"
		parte2 = "   -> C = " + convercionM + "! / " + convercionN + "! * " + convercionDivisor + "!"

		# Factorizando M
		sumando = 0
		while factorialM > 1:
			sumando += 1
			proceso_M += "("+ convercionM +"-"+str(sumando)+")"
			factorialM -= 1
			m *= factorialM

		# Factorizando N
		sumando = 0
		while factorialN > 1:
			sumando += 1
			proceso_N += "("+ convercionN +"-"+str(sumando)+")"
			factorialN -= 1
			n *= factorialN

		# Factorizando M-N
		sumando = 0
		while factorialDivisor > 1:
			sumando += 1
			proceso_divisor += "("+ convercionDivisor +"-"+str(sumando)+")"
			factorialDivisor -=1
			divisor *= factorialDivisor

		parte3 = "   -> C = " + proceso_M + " / " + proceso_N + " * " + proceso_divisor
		parte4 = "   -> C = " + str(m) + " / " + str(n) + " * " + str(divisor)
		parte5 = "   -> C = " + str(m) + " / " + str(n*divisor)

		resultado = m/(n*divisor)

		parte6 = "   -> C = " + str(resultado)

		while True:
			try:
				os.system(borrar)
				print()
				print()
				print("   ***************************************")
				print("   *                                     *")
				print("   *             Combinacion             *")
				print("   *                                     *")
				print("   ***************************************")
				print()
				print("       Formula Lineal: C = m!/(n!*(m-n)!)")
				print()
				print(" Proceso Logico:           Datos: m = " + convercionM + "   n = " + convercionN)
				print()
				
				#Imprimiendo el Proceso
				print(parte1)
				time.sleep(tiempo_espera)
				print(parte2)
				time.sleep(tiempo_espera)
				print(parte3)
				time.sleep(tiempo_espera)
				print(parte4)
				time.sleep(tiempo_espera)
				print(parte5)
				time.sleep(tiempo_espera)
				print(parte6)
				time.sleep(tiempo_espera)

				print()
				print()
				print(" El resultado para la Variacion es: ",resultado)
				print()
				print("--------------------------------------------------------------")
				print()
				print(" Seleccione una Opcion")
				print()
				print(" 1 - Otra Operación")
				print(" 2 - Volver al Menu")
				seleccion = int(input(" ->"))

				if seleccion == 1:
					break
				elif seleccion == 2:
					break
				else:
					Error1()
			
			except ValueError:
				Error2()

		if seleccion == 2:
			break