# Modos de Juego
from funciones import *
from errores import *
from variables_constantes import *

# Exportando Librerias
from random import *
import os
import time

class Modos_de_Juego:
	def __init__():
		pass

	def Modo1():
		Color(blanco)
		iniciar = True
		while iniciar == True:
			try:
				Borrar(limpiar)
				print()
				print("    *********************************************")
				print("    *                                           *")
				print("    *    Bienvenido al Adivinador de Numeros    *")
				print("    *                                           *")
				print("    *********************************************")
				print()
				print(" Piense en un nùmero del 1 al 10")
				print()
				print(" -> Precione 1 - Listo    /    -> Precione 2 - Volver ")
				seleccion = int(input(" -> "))

				if seleccion == 1:
					CargaModo1(limpiar, tiempo_carga_modos)

					while True:
						try:
							Borrar(limpiar)
							print()
							print("   ******************")
							print("   *   Pregunta 1   *")
							print("   ******************")
							print()
							print(" Tu numero es menor que 5?                1 - Si  /  2 - No")
							elegir = int(input(" -> "))

							if elegir == 1:
								Borrar(limpiar)
								print()
								print("   ******************")
								print("   *   Pregunta 2   *")
								print("   ******************")
								print()
								print(" Tu numero multiplicado por 2 da 4?       1 - Si  /  2 - No")
								elegir = int(input(" -> "))

								if elegir == 1:
									Borrar(limpiar)
									print()
									print("   ***********************")
									print("   *    Fin del Juego    *")
									print("   ***********************")
									print()
									print(" Waao... Fue mas facil de lo que pense      Tu numero es: 2       Preguntas: 2")
									break

								elif elegir == 2:
									Borrar(limpiar)
									print()
									print("   ******************")
									print("   *   Pregunta 3   *")
									print("   ******************")
									print()
									print(" Tu numero es par?       1 - Si  /  2 - No")
									elegir = int(input(" -> "))

									if elegir == 1:
										Borrar(limpiar)
										print()
										print("   ***********************")
										print("   *    Fin del Juego    *")
										print("   ***********************")
										print()
										print(" Jummm... Me tomo solo un momento      Tu numero es: 4             Preguntas: 3")
										break

									elif elegir == 2:
										Borrar(limpiar)
										print()
										print("   ******************")
										print("   *   Pregunta 4   *")
										print("   ******************")
										print()
										print(" Tu numero es 1?            1 - Si  /  2 - No")
										elegir = int(input(" -> "))

										if elegir == 1:
											Borrar(limpiar)
											print()
											print("   ***********************")
											print("   *    Fin del Juego    *")
											print("   ***********************")
											print()
											print(" Waao... Si que pensaste bien tu numero      Tu numero es: 1             Preguntas: 4")
											break

										elif elegir == 2:
											Borrar(limpiar)
											print()
											print("   ***********************")
											print("   *    Fin del Juego    *")
											print("   ***********************")
											print()
											print(" Waao... Si que pensaste bien tu numero      Tu numero es: 3             Preguntas: 4")
											break

										else:
											Errores.Error1()

									else:
										Errores.Error1()

								else:
									Errores.Error1()

							elif elegir == 2:
								Borrar(limpiar)
								print()
								print("   ******************")
								print("   *   Pregunta 2   *")
								print("   ******************")
								print()
								print(" Tu numero es mayor que 5?                1 - Si  /  2 - No")
								elegir = int(input(" -> "))

								if elegir == 1:
									Borrar(limpiar)
									print()
									print("   ******************")
									print("   *   Pregunta 3   *")
									print("   ******************")
									print()
									print(" La mitad de tu numero es 3.5?           1 - Si / 2 - No")
									elegir = int(input(" -> "))

									if elegir == 1:
										Borrar(limpiar)
										print()
										print("   ***********************")
										print("   *    Fin del Juego    *")
										print("   ***********************")
										print()
										print(" Waao... Un poco mas de cabeza      Tu numero es: 7       Preguntas: 3")
										break

									elif elegir == 2:
										Borrar(limpiar)
										print()
										print("   ******************")
										print("   *   Pregunta 4   *")
										print("   ******************")
										print()
										print(" Tu numero es par?                1 - Si  /  2 - No")
										elegir = int(input(" -> "))

										if elegir == 1:
											Borrar(limpiar)
											print()
											print("   ******************")
											print("   *   Pregunta 5   *")
											print("   ******************")
											print()
											print(" Tu numero multiplicado por 5 da 50?            1 - Si  /  2 - No")
											elegir = int(input(" -> "))

											if elegir == 1:
												Borrar(limpiar)
												print()
												print("   ***********************")
												print("   *    Fin del Juego    *")
												print("   ***********************")
												print()
												print(" Felicidades... Me hiciste pensar un rato      Tu numero es: 10       Preguntas: 5")
												break

											elif elegir == 2:
												Borrar(limpiar)
												print()
												print("   ******************")
												print("   *   Pregunta 6   *")
												print("   ******************")
												print()
												print(" Tu numero es 8?                  1 - Si  /  2 - No")
												elegir = int(input(" -> "))

												if elegir == 1:
													Borrar(limpiar)
													print()
													print("   ***********************")
													print("   *    Fin del Juego    *")
													print("   ***********************")
													print()
													print(" Felicidades... Me hiciste pensar un rato      Tu numero es: 8       Preguntas: 6")
													break

												elif elegir == 2:
													Borrar(limpiar)
													print()
													print("   ***********************")
													print("   *    Fin del Juego    *")
													print("   ***********************")
													print()
													print(" Felicidades... Me hiciste pensar un rato      Tu numero es: 6       Preguntas: 6")
													break

												else:
													Errores.Error1()

											else:
												Errores.Error1()

										elif elegir == 2:
											Borrar(limpiar)
											print()
											print("   ***********************")
											print("   *    Fin del Juego    *")
											print("   ***********************")
											print()
											print(" Waao... Fue mas facil de lo que pense      Tu numero es: 9       Preguntas: 4")
											break

										else:
											Errores.Error1()

								elif elegir == 2:
									Borrar(limpiar)
									print()
									print("   ***********************")
									print("   *    Fin del Juego    *")
									print("   ***********************")
									print()
									print(" Waao... Fue mas facil de lo que pense      Tu numero es: 5       Preguntas: 2")
									break

								else:
									Errores.Error1()

							else:
								Errores.Error1()

						except ValueError:
							Errores.Error2()

					print()
					input(" -> Precione ENTER para continuar")

					while True:
						try:
							Borrar(limpiar)	
							print()	
							print()
							print(" -> Precione 1 para continuar    /    -> Precione 2 para Salir del Juego")
							elegir = int(input(" -> "))

							if elegir == 1:
								break
							elif elegir == 2:
								iniciar = False
								break
							else:
								Errores.Error1()

						except ValueError:
							Errores.Error2()


				elif seleccion == 2:
					inicio = False
					break
				else:
					Errores.Error1()



			except ValueError:
				Errores.Error2()

	def Modo2():
		Color(verde)
		Iniciar = True
		lanzar = True
		while Iniciar == True:
			try:
				Borrar(limpiar)
				print()
				print("    ****************************************")
				print("    *                                      *")
				print("    *    Bienvenido al Dado Electronico    *")
				print("    *                                      *")
				print("    ****************************************")
				print()

				print(" -> Preciona 1 para Empezar    /    -> Preciona 2 para Volver")
				elegir = int(input(" -> "))


				
				if elegir == 1:
					CargaModo2(limpiar, tiempo_carga_modos)
					input(" -> Precione ENTER para Lanzar")

					while lanzar == True:

						Borrar(limpiar)
						resultado = randint(1,6)

						if resultado == 1:
							print()
							print("              -------------------------")
							print("             |                         |")
							print("             |                         |")
							print("             |                         |")
							print("             |                         |")
							print("             |           * *           |")
							print("             |          * * *          |")
							print("             |           * *           |")
							print("             |                         |")
							print("             |                         |")
							print("             |                         |")
							print("             |                         |")
							print("              -------------------------")
							print()
							print(" -> Precione 1 para volver a lanzar    /    -> Precione 2 para Volver")
							seleccion = int(input(" -> "))
							
							if seleccion == 1:
								pass

							elif seleccion == 2:
								lanzar = False 

							else:
								Errores.Error1()

						elif resultado == 2:
							print()
							print("              -------------------------")
							print("             |                         |")
							print("             |                         |")
							print("             |     * *                 |")
							print("             |    * * *                |")
							print("             |     * *                 |")
							print("             |                         |")
							print("             |                 * *     |")
							print("             |                * * *    |")
							print("             |                 * *     |")
							print("             |                         |")
							print("             |                         |")
							print("              -------------------------")
							print()
							print(" -> Precione 1 para volver a lanzar    /    -> Precione 2 para Volver")
							seleccion = int(input(" -> "))
							
							if seleccion == 1:
								pass

							elif seleccion == 2:
								lanzar = False 

							else:
								Errores.Error1()

						elif resultado == 3:
							print()
							print("              -------------------------")
							print("             |                         |")
							print("             |   * *                   |")
							print("             |  * * *                  |")
							print("             |   * *                   |")
							print("             |           * *           |")
							print("             |          * * *          |")
							print("             |           * *           |")
							print("             |                   * *   |")
							print("             |                  * * *  |")
							print("             |                   * *   |")
							print("             |                         |")
							print("              -------------------------")
							print()
							print(" -> Precione 1 para volver a lanzar    /    -> Precione 2 para Volver")
							seleccion = int(input(" -> "))
							
							if seleccion == 1:
								pass

							elif seleccion == 2:
								lanzar = False 

							else:
								Errores.Error1()


						elif resultado == 4:
							print()
							print("              -------------------------")
							print("             |                         |")
							print("             |   * *             * *   |")
							print("             |  * * *           * * *  |")
							print("             |   * *             * *   |")
							print("             |                         |")
							print("             |                         |")
							print("             |                         |")
							print("             |   * *             * *   |")
							print("             |  * * *           * * *  |")
							print("             |   * *             * *   |")
							print("             |                         |")
							print("              -------------------------")
							print()

							print(" -> Precione 1 para volver a lanzar    /    -> Precione 2 para Volver")
							seleccion = int(input(" -> "))
							
							if seleccion == 1:
								pass

							elif seleccion == 2:
								lanzar = False 

							else:
								Errores.Error1()


						elif resultado == 5:
							print()
							print("              -------------------------")
							print("             |                         |")
							print("             |   * *             * *   |")
							print("             |  * * *           * * *  |")
							print("             |   * *             * *   |")
							print("             |           * *           |")
							print("             |          * * *          |")
							print("             |           * *           |")
							print("             |   * *             * *   |")
							print("             |  * * *           * * *  |")
							print("             |   * *             * *   |")
							print("             |                         |")
							print("              -------------------------")
							print()

							print(" -> Precione 1 para volver a lanzar    /    -> Precione 2 para Volver")
							seleccion = int(input(" -> "))
							
							if seleccion == 1:
								pass

							elif seleccion == 2:
								lanzar = False 

							else:
								Errores.Error1()

						elif resultado == 6:
							print()
							print("              -------------------------")
							print("             |   * *             * *   |")
							print("             |  * * *           * * *  |")
							print("             |   * *             * *   |")
							print("             |                         |")
							print("             |   * *             * *   |")
							print("             |  * * *           * * *  |")
							print("             |   * *             * *   |")
							print("             |                         |")
							print("             |   * *             * *   |")
							print("             |  * * *           * * *  |")
							print("             |   * *             * *   |")
							print("              -------------------------")
							print()

							print(" -> Precione 1 para volver a lanzar    /    -> Precione 2 para Volver")
							seleccion = int(input(" -> "))
							
							if seleccion == 1:
								pass

							elif seleccion == 2:
								lanzar = False 
								break

							else:
								Errores.Error1()




				elif elegir == 2:
					Iniciar == False
					break

				else:
					Errores.Error1()

			except ValueError:
				Errores.Error2()

	def Modo3():
		Color(aguamarina)
		Iniciar = True
		lanzar = True
		while Iniciar == True:
			try:
				Borrar(limpiar)
				print()
				print("    ****************************************")
				print("    *                                      *")
				print("    *    Bienvenido al Dado Electronico    *")
				print("    *                                      *")
				print("    ****************************************")
				print()

				print(" -> Preciona 1 para Empezar    /    -> Preciona 2 para Volver")
				elegir = int(input(" -> "))


				
				if elegir == 1:
					CargaModo2(limpiar, tiempo_carga_modos)
					input(" -> Precione ENTER para Lanzar")

					while lanzar == True:

						Borrar(limpiar)
						dado1 = randint(1,6)
						dado2 = randint(1,6)

						if dado1 == 1 and dado2 == 1:
							print()
							print("              -------------------------               -------------------------")
							print("             |                         |             |                         |")
							print("             |                         |             |                         |")
							print("             |                         |             |                         |")
							print("             |                         |             |                         |")
							print("             |           * *           |             |           * *           |")
							print("             |          * * *          |             |          * * *          |")
							print("             |           * *           |             |           * *           |")
							print("             |                         |             |                         |")
							print("             |                         |             |                         |")
							print("             |                         |             |                         |")
							print("             |                         |             |                         |")
							print("              -------------------------               -------------------------")
							print()
							print(" -> Precione 1 para volver a lanzar    /    -> Precione 2 para Volver")
							seleccion = int(input(" -> "))
							
							if seleccion == 1:
								pass

							elif seleccion == 2:
								lanzar = False 

							else:
								Errores.Error1()

						elif dado1 == 1 and dado2 == 2:
							print()
							print("              -------------------------               -------------------------")
							print("             |                         |             |                         |")
							print("             |                         |             |                         |")
							print("             |                         |             |     * *                 |")
							print("             |                         |             |    * * *                |")
							print("             |           * *           |             |     * *                 |")
							print("             |          * * *          |             |                         |")
							print("             |           * *           |             |                 * *     |")
							print("             |                         |             |                * * *    |")
							print("             |                         |             |                 * *     |")
							print("             |                         |             |                         |")
							print("             |                         |             |                         |")
							print("              -------------------------               -------------------------")
							print()
							print(" -> Precione 1 para volver a lanzar    /    -> Precione 2 para Volver")
							seleccion = int(input(" -> "))
							
							if seleccion == 1:
								pass

							elif seleccion == 2:
								lanzar = False 

							else:
								Errores.Error1()

						elif dado1 == 1 and dado2 == 3:
							print()
							print("              -------------------------               -------------------------")
							print("             |                         |             |                         |")
							print("             |                         |             |    * *                  |")
							print("             |                         |             |   * * *                 |")
							print("             |                         |             |    * *                  |")
							print("             |           * *           |             |           * *           |")
							print("             |          * * *          |             |          * * *          |")
							print("             |           * *           |             |           * *           |")
							print("             |                         |             |                  * *    |")
							print("             |                         |             |                 * * *   |")
							print("             |                         |             |                  * *    |")
							print("             |                         |             |                         |")
							print("              -------------------------               -------------------------")
							print()
							print(" -> Precione 1 para volver a lanzar    /    -> Precione 2 para Volver")
							seleccion = int(input(" -> "))
							
							if seleccion == 1:
								pass

							elif seleccion == 2:
								lanzar = False 

							else:
								Errores.Error1()


						elif dado1 == 1 and dado2 == 4:
							print()
							print("              -------------------------               -------------------------")
							print("             |                         |             |                         |")
							print("             |                         |             |    * *           * *    |")
							print("             |                         |             |   * * *         * * *   |")
							print("             |                         |             |    * *           * *    |")
							print("             |           * *           |             |                         |")
							print("             |          * * *          |             |                         |")
							print("             |           * *           |             |                         |")
							print("             |                         |             |    * *           * *    |")
							print("             |                         |             |   * * *         * * *   |")
							print("             |                         |             |    * *           * *    |")
							print("             |                         |             |                         |")
							print("              -------------------------               -------------------------")
							print()
							print(" -> Precione 1 para volver a lanzar    /    -> Precione 2 para Volver")
							seleccion = int(input(" -> "))
							
							if seleccion == 1:
								pass

							elif seleccion == 2:
								lanzar = False 

							else:
								Errores.Error1()

						elif dado1 == 1 and dado2 == 5:
							print()
							print("              -------------------------               -------------------------")
							print("             |                         |             |                         |")
							print("             |                         |             |    * *           * *    |")
							print("             |                         |             |   * * *         * * *   |")
							print("             |                         |             |    * *           * *    |")
							print("             |           * *           |             |           * *           |")
							print("             |          * * *          |             |          * * *          |")
							print("             |           * *           |             |           * *           |")
							print("             |                         |             |    * *           * *    |")
							print("             |                         |             |   * * *         * * *   |")
							print("             |                         |             |    * *           * *    |")
							print("             |                         |             |                         |")
							print("              -------------------------               -------------------------")
							print()
							print(" -> Precione 1 para volver a lanzar    /    -> Precione 2 para Volver")
							seleccion = int(input(" -> "))
							
							if seleccion == 1:
								pass

							elif seleccion == 2:
								lanzar = False 

							else:
								Errores.Error1()

						elif dado1 == 1 and dado2 == 6:
							print()
							print("              -------------------------               -------------------------")
							print("             |                         |             |    * *           * *    |")
							print("             |                         |             |   * * *         * * *   |")
							print("             |                         |             |    * *           * *    |")
							print("             |                         |             |                         |")
							print("             |           * *           |             |    * *           * *    |")
							print("             |          * * *          |             |   * * *         * * *   |")
							print("             |           * *           |             |    * *           * *    |")
							print("             |                         |             |                         |")
							print("             |                         |             |    * *           * *    |")
							print("             |                         |             |   * * *         * * *   |")
							print("             |                         |             |    * *           * *    |")
							print("              -------------------------               -------------------------")
							print()
							print(" -> Precione 1 para volver a lanzar    /    -> Precione 2 para Volver")
							seleccion = int(input(" -> "))
							
							if seleccion == 1:
								pass

							elif seleccion == 2:
								lanzar = False 

							else:
								Errores.Error1()


						elif dado1 == 2 and dado2 == 1:
							print()
							print("              -------------------------               -------------------------")
							print("             |                         |             |                         |")
							print("             |    * *                  |             |                         |")
							print("             |   * * *                 |             |                         |")
							print("             |    * *                  |             |                         |")
							print("             |                         |             |           * *           |")
							print("             |                         |             |          * * *          |")
							print("             |                         |             |           * *           |")
							print("             |                  * *    |             |                         |")
							print("             |                 * * *   |             |                         |")
							print("             |                  * *    |             |                         |")
							print("             |                         |             |                         |")
							print("              -------------------------               -------------------------")
							print()
							print(" -> Precione 1 para volver a lanzar    /    -> Precione 2 para Volver")
							seleccion = int(input(" -> "))
							
							if seleccion == 1:
								pass

							elif seleccion == 2:
								lanzar = False 

							else:
								Errores.Error1()

						elif dado1 == 2 and dado2 == 2:
							print()
							print("              -------------------------               -------------------------")
							print("             |                         |             |                         |")
							print("             |    * *                  |             |                         |")
							print("             |   * * *                 |             |     * *                 |")
							print("             |    * *                  |             |    * * *                |")
							print("             |                         |             |     * *                 |")
							print("             |                         |             |                         |")
							print("             |                         |             |                 * *     |")
							print("             |                  * *    |             |                * * *    |")
							print("             |                 * * *   |             |                 * *     |")
							print("             |                  * *    |             |                         |")
							print("             |                         |             |                         |")
							print("              -------------------------               -------------------------")
							print()
							print(" -> Precione 1 para volver a lanzar    /    -> Precione 2 para Volver")
							seleccion = int(input(" -> "))
							
							if seleccion == 1:
								pass

							elif seleccion == 2:
								lanzar = False 

							else:
								Errores.Error1()

						elif dado1 == 2 and dado2 == 3:
							print()
							print("              -------------------------               -------------------------")
							print("             |                         |             |                         |")
							print("             |    * *                  |             |    * *                  |")
							print("             |   * * *                 |             |   * * *                 |")
							print("             |    * *                  |             |    * *                  |")
							print("             |                         |             |           * *           |")
							print("             |                         |             |          * * *          |")
							print("             |                         |             |           * *           |")
							print("             |                  * *    |             |                  * *    |")
							print("             |                 * * *   |             |                 * * *   |")
							print("             |                  * *    |             |                  * *    |")
							print("             |                         |             |                         |")
							print("              -------------------------               -------------------------")
							print()
							print(" -> Precione 1 para volver a lanzar    /    -> Precione 2 para Volver")
							seleccion = int(input(" -> "))
							
							if seleccion == 1:
								pass

							elif seleccion == 2:
								lanzar = False 

							else:
								Errores.Error1()


						elif dado1 == 2 and dado2 == 4:
							print()
							print("              -------------------------               -------------------------")
							print("             |                         |             |                         |")
							print("             |    * *                  |             |    * *           * *    |")
							print("             |   * * *                 |             |   * * *         * * *   |")
							print("             |    * *                  |             |    * *           * *    |")
							print("             |                         |             |                         |")
							print("             |                         |             |                         |")
							print("             |                         |             |                         |")
							print("             |                  * *    |             |    * *           * *    |")
							print("             |                 * * *   |             |   * * *         * * *   |")
							print("             |                  * *    |             |    * *           * *    |")
							print("             |                         |             |                         |")
							print("              -------------------------               -------------------------")
							print()
							print(" -> Precione 1 para volver a lanzar    /    -> Precione 2 para Volver")
							seleccion = int(input(" -> "))
							
							if seleccion == 1:
								pass

							elif seleccion == 2:
								lanzar = False 

							else:
								Errores.Error1()

						elif dado1 == 2 and dado2 == 5:
							print()
							print("              -------------------------               -------------------------")
							print("             |                         |             |                         |")
							print("             |    * *                  |             |    * *           * *    |")
							print("             |   * * *                 |             |   * * *         * * *   |")
							print("             |    * *                  |             |    * *           * *    |")
							print("             |                         |             |           * *           |")
							print("             |                         |             |          * * *          |")
							print("             |                         |             |           * *           |")
							print("             |                  * *    |             |    * *           * *    |")
							print("             |                 * * *   |             |   * * *         * * *   |")
							print("             |                  * *    |             |    * *           * *    |")
							print("             |                         |             |                         |")
							print("              -------------------------               -------------------------")
							print()
							print(" -> Precione 1 para volver a lanzar    /    -> Precione 2 para Volver")
							seleccion = int(input(" -> "))
							
							if seleccion == 1:
								pass

							elif seleccion == 2:
								lanzar = False 

							else:
								Errores.Error1()

						elif dado1 == 2 and dado2 == 6:
							print()
							print("              -------------------------               -------------------------")
							print("             |                         |             |    * *           * *    |")
							print("             |    * *                  |             |   * * *         * * *   |")
							print("             |   * * *                 |             |    * *           * *    |")
							print("             |    * *                  |             |                         |")
							print("             |                         |             |    * *           * *    |")
							print("             |                         |             |   * * *         * * *   |")
							print("             |                         |             |    * *           * *    |")
							print("             |                  * *    |             |                         |")
							print("             |                 * * *   |             |    * *           * *    |")
							print("             |                  * *    |             |   * * *         * * *   |")
							print("             |                         |             |    * *           * *    |")
							print("              -------------------------               -------------------------")
							print()
							print(" -> Precione 1 para volver a lanzar    /    -> Precione 2 para Volver")
							seleccion = int(input(" -> "))
							
							if seleccion == 1:
								pass

							elif seleccion == 2:
								lanzar = False 

							else:
								Errores.Error1()


						elif dado1 == 3 and dado2 == 1:
							print()
							print("              -------------------------               -------------------------")
							print("             |                         |             |                         |")
							print("             |    * *                  |             |                         |")
							print("             |   * * *                 |             |                         |")
							print("             |    * *                  |             |                         |")
							print("             |           * *           |             |           * *           |")
							print("             |          * * *          |             |          * * *          |")
							print("             |           * *           |             |           * *           |")
							print("             |                  * *    |             |                         |")
							print("             |                 * * *   |             |                         |")
							print("             |                  * *    |             |                         |")
							print("             |                         |             |                         |")
							print("              -------------------------               -------------------------")
							print()
							print(" -> Precione 1 para volver a lanzar    /    -> Precione 2 para Volver")
							seleccion = int(input(" -> "))
							
							if seleccion == 1:
								pass

							elif seleccion == 2:
								lanzar = False 

							else:
								Errores.Error1()

						elif dado1 == 3 and dado2 == 2:
							print()
							print("              -------------------------               -------------------------")
							print("             |                         |             |                         |")
							print("             |    * *                  |             |                         |")
							print("             |   * * *                 |             |     * *                 |")
							print("             |    * *                  |             |    * * *                |")
							print("             |           * *           |             |     * *                 |")
							print("             |          * * *          |             |                         |")
							print("             |           * *           |             |                 * *     |")
							print("             |                  * *    |             |                * * *    |")
							print("             |                 * * *   |             |                 * *     |")
							print("             |                  * *    |             |                         |")
							print("             |                         |             |                         |")
							print("              -------------------------               -------------------------")
							print()
							print(" -> Precione 1 para volver a lanzar    /    -> Precione 2 para Volver")
							seleccion = int(input(" -> "))
							
							if seleccion == 1:
								pass

							elif seleccion == 2:
								lanzar = False 

							else:
								Errores.Error1()

						elif dado1 == 3 and dado2 == 3:
							print()
							print("              -------------------------               -------------------------")
							print("             |                         |             |                         |")
							print("             |    * *                  |             |    * *                  |")
							print("             |   * * *                 |             |   * * *                 |")
							print("             |    * *                  |             |    * *                  |")
							print("             |           * *           |             |           * *           |")
							print("             |          * * *          |             |          * * *          |")
							print("             |           * *           |             |           * *           |")
							print("             |                  * *    |             |                  * *    |")
							print("             |                 * * *   |             |                 * * *   |")
							print("             |                  * *    |             |                  * *    |")
							print("             |                         |             |                         |")
							print("              -------------------------               -------------------------")
							print()
							print(" -> Precione 1 para volver a lanzar    /    -> Precione 2 para Volver")
							seleccion = int(input(" -> "))
							
							if seleccion == 1:
								pass

							elif seleccion == 2:
								lanzar = False 

							else:
								Errores.Error1()


						elif dado1 == 3 and dado2 == 4:
							print()
							print("              -------------------------               -------------------------")
							print("             |                         |             |                         |")
							print("             |    * *                  |             |    * *           * *    |")
							print("             |   * * *                 |             |   * * *         * * *   |")
							print("             |    * *                  |             |    * *           * *    |")
							print("             |           * *           |             |                         |")
							print("             |          * * *          |             |                         |")
							print("             |           * *           |             |                         |")
							print("             |                  * *    |             |    * *           * *    |")
							print("             |                 * * *   |             |   * * *         * * *   |")
							print("             |                  * *    |             |    * *           * *    |")
							print("             |                         |             |                         |")
							print("              -------------------------               -------------------------")
							print()
							print(" -> Precione 1 para volver a lanzar    /    -> Precione 2 para Volver")
							seleccion = int(input(" -> "))
							
							if seleccion == 1:
								pass

							elif seleccion == 2:
								lanzar = False 

							else:
								Errores.Error1()

						elif dado1 == 3 and dado2 == 5:
							print()
							print("              -------------------------               -------------------------")
							print("             |                         |             |                         |")
							print("             |    * *                  |             |    * *           * *    |")
							print("             |   * * *                 |             |   * * *         * * *   |")
							print("             |    * *                  |             |    * *           * *    |")
							print("             |           * *           |             |           * *           |")
							print("             |          * * *          |             |          * * *          |")
							print("             |           * *           |             |           * *           |")
							print("             |                  * *    |             |    * *           * *    |")
							print("             |                 * * *   |             |   * * *         * * *   |")
							print("             |                  * *    |             |    * *           * *    |")
							print("             |                         |             |                         |")
							print("              -------------------------               -------------------------")
							print()
							print(" -> Precione 1 para volver a lanzar    /    -> Precione 2 para Volver")
							seleccion = int(input(" -> "))
							
							if seleccion == 1:
								pass

							elif seleccion == 2:
								lanzar = False 

							else:
								Errores.Error1()

						elif dado1 == 3 and dado2 == 6:
							print()
							print("              -------------------------               -------------------------")
							print("             |                         |             |    * *           * *    |")
							print("             |    * *                  |             |   * * *         * * *   |")
							print("             |   * * *                 |             |    * *           * *    |")
							print("             |    * *                  |             |                         |")
							print("             |           * *           |             |    * *           * *    |")
							print("             |          * * *          |             |   * * *         * * *   |")
							print("             |           * *           |             |    * *           * *    |")
							print("             |                  * *    |             |                         |")
							print("             |                 * * *   |             |    * *           * *    |")
							print("             |                  * *    |             |   * * *         * * *   |")
							print("             |                         |             |    * *           * *    |")
							print("              -------------------------               -------------------------")
							print()
							print(" -> Precione 1 para volver a lanzar    /    -> Precione 2 para Volver")
							seleccion = int(input(" -> "))
							
							if seleccion == 1:
								pass

							elif seleccion == 2:
								lanzar = False 

							else:
								Errores.Error1()

						elif dado1 == 4 and dado2 == 1:
							print()
							print("              -------------------------               -------------------------")
							print("             |                         |             |                         |")
							print("             |    * *           * *    |             |                         |")
							print("             |   * * *         * * *   |             |                         |")
							print("             |    * *           * *    |             |                         |")
							print("             |                         |             |           * *           |")
							print("             |                         |             |          * * *          |")
							print("             |                         |             |           * *           |")
							print("             |    * *           * *    |             |                         |")
							print("             |   * * *         * * *   |             |                         |")
							print("             |    * *           * *    |             |                         |")
							print("             |                         |             |                         |")
							print("              -------------------------               -------------------------")
							print()
							print(" -> Precione 1 para volver a lanzar    /    -> Precione 2 para Volver")
							seleccion = int(input(" -> "))
							
							if seleccion == 1:
								pass

							elif seleccion == 2:
								lanzar = False 

							else:
								Errores.Error1()

						elif dado1 == 4 and dado2 == 2:
							print()
							print("              -------------------------               -------------------------")
							print("             |                         |             |                         |")
							print("             |    * *           * *    |             |                         |")
							print("             |   * * *         * * *   |             |     * *                 |")
							print("             |    * *           * *    |             |    * * *                |")
							print("             |                         |             |     * *                 |")
							print("             |                         |             |                         |")
							print("             |                         |             |                 * *     |")
							print("             |    * *           * *    |             |                * * *    |")
							print("             |   * * *         * * *   |             |                 * *     |")
							print("             |    * *           * *    |             |                         |")
							print("             |                         |             |                         |")
							print("              -------------------------               -------------------------")
							print()
							print(" -> Precione 1 para volver a lanzar    /    -> Precione 2 para Volver")
							seleccion = int(input(" -> "))
							
							if seleccion == 1:
								pass

							elif seleccion == 2:
								lanzar = False 

							else:
								Errores.Error1()

						elif dado1 == 4 and dado2 == 3:
							print()
							print("              -------------------------               -------------------------")
							print("             |                         |             |                         |")
							print("             |    * *           * *    |             |    * *                  |")
							print("             |   * * *         * * *   |             |   * * *                 |")
							print("             |    * *           * *    |             |    * *                  |")
							print("             |                         |             |           * *           |")
							print("             |                         |             |          * * *          |")
							print("             |                         |             |           * *           |")
							print("             |    * *           * *    |             |                  * *    |")
							print("             |   * * *         * * *   |             |                 * * *   |")
							print("             |    * *           * *    |             |                  * *    |")
							print("             |                         |             |                         |")
							print("              -------------------------               -------------------------")
							print()
							print(" -> Precione 1 para volver a lanzar    /    -> Precione 2 para Volver")
							seleccion = int(input(" -> "))
							
							if seleccion == 1:
								pass

							elif seleccion == 2:
								lanzar = False 

							else:
								Errores.Error1()


						elif dado1 == 4 and dado2 == 4:
							print()
							print("              -------------------------               -------------------------")
							print("             |                         |             |                         |")
							print("             |    * *           * *    |             |    * *           * *    |")
							print("             |   * * *         * * *   |             |   * * *         * * *   |")
							print("             |    * *           * *    |             |    * *           * *    |")
							print("             |                         |             |                         |")
							print("             |                         |             |                         |")
							print("             |                         |             |                         |")
							print("             |    * *           * *    |             |    * *           * *    |")
							print("             |   * * *         * * *   |             |   * * *         * * *   |")
							print("             |    * *           * *    |             |    * *           * *    |")
							print("             |                         |             |                         |")
							print("              -------------------------               -------------------------")
							print()
							print(" -> Precione 1 para volver a lanzar    /    -> Precione 2 para Volver")
							seleccion = int(input(" -> "))
							
							if seleccion == 1:
								pass

							elif seleccion == 2:
								lanzar = False 

							else:
								Errores.Error1()

						elif dado1 == 4 and dado2 == 5:
							print()
							print("              -------------------------               -------------------------")
							print("             |                         |             |                         |")
							print("             |    * *           * *    |             |    * *           * *    |")
							print("             |   * * *         * * *   |             |   * * *         * * *   |")
							print("             |    * *           * *    |             |    * *           * *    |")
							print("             |                         |             |           * *           |")
							print("             |                         |             |          * * *          |")
							print("             |                         |             |           * *           |")
							print("             |    * *           * *    |             |    * *           * *    |")
							print("             |   * * *         * * *   |             |   * * *         * * *   |")
							print("             |    * *           * *    |             |    * *           * *    |")
							print("             |                         |             |                         |")
							print("              -------------------------               -------------------------")
							print()
							print(" -> Precione 1 para volver a lanzar    /    -> Precione 2 para Volver")
							seleccion = int(input(" -> "))
							
							if seleccion == 1:
								pass

							elif seleccion == 2:
								lanzar = False 

							else:
								Errores.Error1()

						elif dado1 == 4 and dado2 == 6:
							print()
							print("              -------------------------               -------------------------")
							print("             |                         |             |    * *           * *    |")
							print("             |    * *           * *    |             |   * * *         * * *   |")
							print("             |   * * *         * * *   |             |    * *           * *    |")
							print("             |    * *           * *    |             |                         |")
							print("             |                         |             |    * *           * *    |")
							print("             |                         |             |   * * *         * * *   |")
							print("             |                         |             |    * *           * *    |")
							print("             |    * *           * *    |             |                         |")
							print("             |   * * *         * * *   |             |    * *           * *    |")
							print("             |    * *           * *    |             |   * * *         * * *   |")
							print("             |                         |             |    * *           * *    |")
							print("              -------------------------               -------------------------")
							print()
							print(" -> Precione 1 para volver a lanzar    /    -> Precione 2 para Volver")
							seleccion = int(input(" -> "))
							
							if seleccion == 1:
								pass

							elif seleccion == 2:
								lanzar = False 

							else:
								Errores.Error1()

						elif dado1 == 5 and dado2 == 1:
							print()
							print("              -------------------------               -------------------------")
							print("             |                         |             |                         |")
							print("             |    * *           * *    |             |                         |")
							print("             |   * * *         * * *   |             |                         |")
							print("             |    * *           * *    |             |                         |")
							print("             |           * *           |             |           * *           |")
							print("             |          * * *          |             |          * * *          |")
							print("             |           * *           |             |           * *           |")
							print("             |    * *           * *    |             |                         |")
							print("             |   * * *         * * *   |             |                         |")
							print("             |    * *           * *    |             |                         |")
							print("             |                         |             |                         |")
							print("              -------------------------               -------------------------")
							print()
							print(" -> Precione 1 para volver a lanzar    /    -> Precione 2 para Volver")
							seleccion = int(input(" -> "))
							
							if seleccion == 1:
								pass

							elif seleccion == 2:
								lanzar = False 

							else:
								Errores.Error1()

						elif dado1 == 5 and dado2 == 2:
							print()
							print("              -------------------------               -------------------------")
							print("             |                         |             |                         |")
							print("             |    * *           * *    |             |                         |")
							print("             |   * * *         * * *   |             |     * *                 |")
							print("             |    * *           * *    |             |    * * *                |")
							print("             |           * *           |             |     * *                 |")
							print("             |          * * *          |             |                         |")
							print("             |           * *           |             |                 * *     |")
							print("             |    * *           * *    |             |                * * *    |")
							print("             |   * * *         * * *   |             |                 * *     |")
							print("             |    * *           * *    |             |                         |")
							print("             |                         |             |                         |")
							print("              -------------------------               -------------------------")
							print()
							print(" -> Precione 1 para volver a lanzar    /    -> Precione 2 para Volver")
							seleccion = int(input(" -> "))
							
							if seleccion == 1:
								pass

							elif seleccion == 2:
								lanzar = False 

							else:
								Errores.Error1()

						elif dado1 == 5 and dado2 == 3:
							print()
							print("              -------------------------               -------------------------")
							print("             |                         |             |                         |")
							print("             |    * *           * *    |             |    * *                  |")
							print("             |   * * *         * * *   |             |   * * *                 |")
							print("             |    * *           * *    |             |    * *                  |")
							print("             |           * *           |             |           * *           |")
							print("             |          * * *          |             |          * * *          |")
							print("             |           * *           |             |           * *           |")
							print("             |    * *           * *    |             |                  * *    |")
							print("             |   * * *         * * *   |             |                 * * *   |")
							print("             |    * *           * *    |             |                  * *    |")
							print("             |                         |             |                         |")
							print("              -------------------------               -------------------------")
							print()
							print(" -> Precione 1 para volver a lanzar    /    -> Precione 2 para Volver")
							seleccion = int(input(" -> "))
							
							if seleccion == 1:
								pass

							elif seleccion == 2:
								lanzar = False 

							else:
								Errores.Error1()


						elif dado1 == 5 and dado2 == 4:
							print()
							print("              -------------------------               -------------------------")
							print("             |                         |             |                         |")
							print("             |    * *           * *    |             |    * *           * *    |")
							print("             |   * * *         * * *   |             |   * * *         * * *   |")
							print("             |    * *           * *    |             |    * *           * *    |")
							print("             |           * *           |             |                         |")
							print("             |          * * *          |             |                         |")
							print("             |           * *           |             |                         |")
							print("             |    * *           * *    |             |    * *           * *    |")
							print("             |   * * *         * * *   |             |   * * *         * * *   |")
							print("             |    * *           * *    |             |    * *           * *    |")
							print("             |                         |             |                         |")
							print("              -------------------------               -------------------------")
							print()
							print(" -> Precione 1 para volver a lanzar    /    -> Precione 2 para Volver")
							seleccion = int(input(" -> "))
							
							if seleccion == 1:
								pass

							elif seleccion == 2:
								lanzar = False 

							else:
								Errores.Error1()

						elif dado1 == 5 and dado2 == 5:
							print()
							print("              -------------------------               -------------------------")
							print("             |                         |             |                         |")
							print("             |    * *           * *    |             |    * *           * *    |")
							print("             |   * * *         * * *   |             |   * * *         * * *   |")
							print("             |    * *           * *    |             |    * *           * *    |")
							print("             |           * *           |             |           * *           |")
							print("             |          * * *          |             |          * * *          |")
							print("             |           * *           |             |           * *           |")
							print("             |    * *           * *    |             |    * *           * *    |")
							print("             |   * * *         * * *   |             |   * * *         * * *   |")
							print("             |    * *           * *    |             |    * *           * *    |")
							print("             |                         |             |                         |")
							print("              -------------------------               -------------------------")
							print()
							print(" -> Precione 1 para volver a lanzar    /    -> Precione 2 para Volver")
							seleccion = int(input(" -> "))
							
							if seleccion == 1:
								pass

							elif seleccion == 2:
								lanzar = False 

							else:
								Errores.Error1()

						elif dado1 == 5 and dado2 == 6:
							print()
							print("              -------------------------               -------------------------")
							print("             |                         |             |    * *           * *    |")
							print("             |    * *           * *    |             |   * * *         * * *   |")
							print("             |   * * *         * * *   |             |    * *           * *    |")
							print("             |    * *           * *    |             |                         |")
							print("             |           * *           |             |    * *           * *    |")
							print("             |          * * *          |             |   * * *         * * *   |")
							print("             |           * *           |             |    * *           * *    |")
							print("             |    * *           * *    |             |                         |")
							print("             |   * * *         * * *   |             |    * *           * *    |")
							print("             |    * *           * *    |             |   * * *         * * *   |")
							print("             |                         |             |    * *           * *    |")
							print("              -------------------------               -------------------------")
							print()
							print(" -> Precione 1 para volver a lanzar    /    -> Precione 2 para Volver")
							seleccion = int(input(" -> "))
							
							if seleccion == 1:
								pass

							elif seleccion == 2:
								lanzar = False 

							else:
								Errores.Error1()


						elif dado1 == 6 and dado2 == 1:
							print()
							print("              -------------------------               -------------------------")
							print("             |    * *           * *    |             |                         |")
							print("             |   * * *         * * *   |             |                         |")
							print("             |    * *           * *    |             |                         |")
							print("             |                         |             |                         |")
							print("             |    * *           * *    |             |           * *           |")
							print("             |   * * *         * * *   |             |          * * *          |")
							print("             |    * *           * *    |             |           * *           |")
							print("             |                         |             |                         |")
							print("             |    * *           * *    |             |                         |")
							print("             |   * * *         * * *   |             |                         |")
							print("             |    * *           * *    |             |                         |")
							print("              -------------------------               -------------------------")
							print()
							print(" -> Precione 1 para volver a lanzar    /    -> Precione 2 para Volver")
							seleccion = int(input(" -> "))
							
							if seleccion == 1:
								pass

							elif seleccion == 2:
								lanzar = False 

							else:
								Errores.Error1()

						elif dado1 == 6 and dado2 == 2:
							print()
							print("              -------------------------               -------------------------")
							print("             |    * *           * *    |             |                         |")
							print("             |   * * *         * * *   |             |                         |")
							print("             |    * *           * *    |             |     * *                 |")
							print("             |                         |             |    * * *                |")
							print("             |    * *           * *    |             |     * *                 |")
							print("             |   * * *         * * *   |             |                         |")
							print("             |    * *           * *    |             |                 * *     |")
							print("             |                         |             |                * * *    |")
							print("             |    * *           * *    |             |                 * *     |")
							print("             |   * * *         * * *   |             |                         |")
							print("             |    * *           * *    |             |                         |")
							print("              -------------------------               -------------------------")
							print()
							print(" -> Precione 1 para volver a lanzar    /    -> Precione 2 para Volver")
							seleccion = int(input(" -> "))
							
							if seleccion == 1:
								pass

							elif seleccion == 2:
								lanzar = False 

							else:
								Errores.Error1()

						elif dado1 == 6 and dado2 == 3:
							print()
							print("              -------------------------               -------------------------")
							print("             |    * *           * *    |             |                         |")
							print("             |   * * *         * * *   |             |    * *                  |")
							print("             |    * *           * *    |             |   * * *                 |")
							print("             |                         |             |    * *                  |")
							print("             |    * *           * *    |             |           * *           |")
							print("             |   * * *         * * *   |             |          * * *          |")
							print("             |    * *           * *    |             |           * *           |")
							print("             |                         |             |                  * *    |")
							print("             |    * *           * *    |             |                 * * *   |")
							print("             |   * * *         * * *   |             |                  * *    |")
							print("             |    * *           * *    |             |                         |")
							print("              -------------------------               -------------------------")
							print()
							print(" -> Precione 1 para volver a lanzar    /    -> Precione 2 para Volver")
							seleccion = int(input(" -> "))
							
							if seleccion == 1:
								pass

							elif seleccion == 2:
								lanzar = False 

							else:
								Errores.Error1()


						elif dado1 == 6 and dado2 == 4:
							print()
							print("              -------------------------               -------------------------")
							print("             |    * *           * *    |             |                         |")
							print("             |   * * *         * * *   |             |    * *           * *    |")
							print("             |    * *           * *    |             |   * * *         * * *   |")
							print("             |                         |             |    * *           * *    |")
							print("             |    * *           * *    |             |                         |")
							print("             |   * * *         * * *   |             |                         |")
							print("             |    * *           * *    |             |                         |")
							print("             |                         |             |    * *           * *    |")
							print("             |    * *           * *    |             |   * * *         * * *   |")
							print("             |   * * *         * * *   |             |    * *           * *    |")
							print("             |    * *           * *    |             |                         |")
							print("              -------------------------               -------------------------")
							print()
							print(" -> Precione 1 para volver a lanzar    /    -> Precione 2 para Volver")
							seleccion = int(input(" -> "))
							
							if seleccion == 1:
								pass

							elif seleccion == 2:
								lanzar = False 

							else:
								Errores.Error1()

						elif dado1 == 6 and dado2 == 5:
							print()
							print("              -------------------------               -------------------------")
							print("             |    * *           * *    |             |                         |")
							print("             |   * * *         * * *   |             |    * *           * *    |")
							print("             |    * *           * *    |             |   * * *         * * *   |")
							print("             |                         |             |    * *           * *    |")
							print("             |    * *           * *    |             |           * *           |")
							print("             |   * * *         * * *   |             |          * * *          |")
							print("             |    * *           * *    |             |           * *           |")
							print("             |                         |             |    * *           * *    |")
							print("             |    * *           * *    |             |   * * *         * * *   |")
							print("             |   * * *         * * *   |             |    * *           * *    |")
							print("             |    * *           * *    |             |                         |")
							print("              -------------------------               -------------------------")
							print()
							print(" -> Precione 1 para volver a lanzar    /    -> Precione 2 para Volver")
							seleccion = int(input(" -> "))
							
							if seleccion == 1:
								pass

							elif seleccion == 2:
								lanzar = False 

							else:
								Errores.Error1()

						elif dado1 == 6 and dado2 == 6:
							print()
							print("              -------------------------               -------------------------")
							print("             |    * *           * *    |             |    * *           * *    |")
							print("             |   * * *         * * *   |             |   * * *         * * *   |")
							print("             |    * *           * *    |             |    * *           * *    |")
							print("             |                         |             |                         |")
							print("             |    * *           * *    |             |    * *           * *    |")
							print("             |   * * *         * * *   |             |   * * *         * * *   |")
							print("             |    * *           * *    |             |    * *           * *    |")
							print("             |                         |             |                         |")
							print("             |    * *           * *    |             |    * *           * *    |")
							print("             |   * * *         * * *   |             |   * * *         * * *   |")
							print("             |    * *           * *    |             |    * *           * *    |")
							print("              -------------------------               -------------------------")
							print()
							print(" -> Precione 1 para volver a lanzar    /    -> Precione 2 para Volver")
							seleccion = int(input(" -> "))
							
							if seleccion == 1:
								pass

							elif seleccion == 2:
								lanzar = False 

							else:
								Errores.Error1()





				elif elegir == 2:
					Iniciar == False
					break

				else:
					Errores.Error1()

			except ValueError:
				Errores.Error2()

