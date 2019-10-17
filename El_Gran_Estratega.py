import os; import time; import random

# Esta Clase guarda todos los Errores que se pueden presentar
class Errores():
	def __init__(self):
		pass

	def Error1(self):
		tiempo = 5
		print("-> Error 1: Este campo solo permite valores numericos")
		time.sleep(tiempo)

	def Error2(self):
		tiempo = 5
		print("->   Error 2: Seleccione una opción disponible")
		time.sleep(tiempo)

	def Error3(self):
		tiempo = 5
		print("->   Error 3: Usuario o Contraseña Incorrecta")
		print("->   Puede que este Usuario no exista. Registrate")
		time.sleep(tiempo)

# Área de Registro
def Registro(usuario, hp, inicio):
	hp = 1000
	inicio = True
	usuario = input("Nombre de Usuario: ")
	contrasena = input("Ingrese una Contraseña: ")
	nombre = input("Escriba su nombre: ")
	apellido = input("Escriba su apellido: ")
	edad = input("Escriba su edad: ")
	correo = input("Ingrese su Correo: ")

	jugador = open(usuario + '.txt', 'w')
	jugador.write(usuario)
	
	contra = open(usuario + "_CT" + '.txt', 'w')
	contra.write(contrasena)

	experiencia = open(usuario + "_HP" + '.txt', 'w')
	experiencia.write(str(hp))

	datos = open(usuario + "_DT" + '.txt', 'w')
	datos.write(
		"\n             Datos del Jugador" +
		"\n" +
		"\n   Nombre de Usuario:    " + usuario +
		"\n   Contraseña:                  " + contrasena +
		"\n   Nombre:                         " + nombre + 
		"\n   Apellido:                         " + apellido + 
		"\n   Edad:                              " + edad + "Años" +
		"\n   Correo:                           " + correo)

	lista = open("Lista de Usuarios.txt", 'r')
	usuarios = lista.read()
	usuarios += "\n" + usuario
	lista = open("Lista de Usuarios.txt", 'w')
	lista.write(usuarios)

	return (usuario, hp, inicio)

# Área de Inicio de Sesión
def Inicio_Sesion(usuario, hp, inicio):
	# Iniciando Variables
	contra = ""; borrar = "cls"
	# Objeto Errores
	errores = Errores()

	while True:
		os.system(borrar)
		try:
			print()
			print()
			print("      ************************************")
			print("      *                                  *")
			print("      *          Iniciar Sesión          *")
			print("      *                                  *")
			print("      ************************************")
			print("          Para Salir ingrese Usuario 5")
			print()

			usuario = input("-> Ingrese su nombre de Usuario: ")
			contrasena = input("-> Ingrese su Contraseña: ")

			if usuario == "5":
				return usuario, hp, inicio
				break

			else:
				f = open(usuario + "_CT" + '.txt', 'r')
				contra = f.read()

				if contrasena == contra:

					hptxt = open(usuario + "_HP" + '.txt', 'r')
					hp = int(hptxt.read())
					inicio = True
					hp += 50
					return usuario, hp, inicio

		except ValueError:
			errores.Error3()

# Área para seleccionar el Modo de Juego
def MenuSeleccion(seleccion):

	# Declaración e iniciación de variables locales
	borrar = "cls"

	# Objeto para los Errores
	errores = Errores()

	# Inicio de Selección
	while True:
		try:
			os.system(borrar)
			print("""
				*********************************************
				*                                           *
				*      Bienvenido al Menú de Selección      *
				*                                           *
				*********************************************

	 ---------------------------------------------------------------------------------------
	|                                                                                       |
	|                           Seleccione el modo de juego deseado                         |
	|                                                                                       |
	|    -------------------------------------------------------------------------------    |
	|   |                           En este modo se enfrentarán en un uno contra uno    |   |
	|   | 1 - 1 VS 1                el jugador podrá renunciar luego de completar las   |   |
	|   |                           5 rondas si este está perdiendo.                    |   |
	|    -------------------------------------------------------------------------------    |
	|   |                           En este modo se enfrentarán en grupos de dos. Solo  |   |
	|   |                           se renuncia si están desúés de la ronda 10 si el    |   |
	|   | 2 - 2 VS 2                equipo que va perdiendo lo decide. La experiencia   |   |
	|   |                           (HP) ganada se respartirá en partes iguales a los   |   |
	|   |                           Ganadores.                                          |   |
	|    -------------------------------------------------------------------------------    |
	|   |                           En este modo se enfrentarán en un 1 VS 1 hasta que  |   |
	|   | 3 - Duelo a Muerte        uno de los dos jugadores quede en 0HP.              |   |
	|   |                           No se puede renunciar de la partida.                |   |
	|    -------------------------------------------------------------------------------    |
	|   |                           En este modo se enfrentarán hasta 4 jugadores en	|   |
	|   | 4 - Contra Todos          una batalla. Después de la 6 ronda los jugadores    |   |
	|   |                           que vallan perdierdo podrán renunciar.              |   |
	|    -------------------------------------------------------------------------------	|
	|   |                           En este mose se enfrentan hasta 6 jugadores en una  |   |
	|   | 5 - Battle Royale         batalla a muerte. Los jugadores podrán renunciar    |   |
	|   |                           después de la ronda 20.                             |   |
	|    -------------------------------------------------------------------------------    |
	|   | 6 - Salir                                                                     |   |
	|    -------------------------------------------------------------------------------    |
	|                                                                                       |
	 ---------------------------------------------------------------------------------------
	 """)
			seleccion = int(input("-> "))

			if 1 <= seleccion <= 6:
				return seleccion
				break
			else:
				errores.Error2()

		except ValueError:
			errores.Error1()
 
# Modo de Juego 1: Uno contra Uno           + Agregar Funciones de la Ruleta
def Modo_De_Juego_1(usuario1,hp1):
	# Declaración de Variables Locales
	usuario2 = ""; hp2 = 0; iniciar = False; borrar = 'cls'

	# Inicio del Jugador 2
	while iniciar == False:
		os.system(borrar)
		print("   Esperando a Jugador 2")
		print("   Jugador 1: ", usuario1, "->   HP: ", hp1)
		print("   Jugador 2: Presione 2 para Iniciar Sesión")
		print()
		seleccion = int(input("-> "))

		if seleccion == 2:
			usuario2, hp2, iniciar = Inicio_Sesion(usuario2, hp2, iniciar)
	#----------------------------------------------------------------------------

	# Menú de Confirmación
	while True:
		os.system(borrar)
		print("   Listos Para el Combate")
		print("   Jugador 1: ", usuario1, "->   HP: ", hp1)
		print("   Jugador 2: ", usuario2, "->   HP: ", hp2)
		print("")
		print("   1 - Iniciar Combate")
		print("   2 - Salir")    
		print("   Nota: Una vez que inician no podrán Abandonar")
		print()
		seleccion = int(input("-> "))

		# Combate
		if seleccion == 1:
			print()
			print("                       ", usuario1, "  VS  ", usuario2)
			print()
			print("-> Espere un Momento...")
			time.sleep(5)
			os.system(borrar)

			#---------------------------------------------------

			# Iniciando Variales
			energia1 = 1; energia2 = 1; combate = True
			turno = 1;

			# Variables de Ataques Globales
			ataque_basico = 5; ataque_medio = 15
			ataque_fuerte = 25; ruleta1 = 3; ruleta2 = 3

			# Variables de Hechizos
			# Hechizo 5: Robo de energia Hechizo 6: Robo de Ruleta
			hechizo1 = 100; hechizo2 = 30; hechizo3 = 75; hechizo4 = 0; hechizo5 = 0; hechizo6 = 50
			espacio1_J1 = 0; espacio2_J1 = 0; espacio3_J1 = 0;
			espacio1_J2 = 0; espacio2_J2 = 0; espacio3_J2 = 0;

			#---------------------------------------------------
			# Selección de Hechizos
			usuario1,usuario2,turno,espacio1_J1,espacio2_J1,espacio3_J1,espacio1_J2,espacio2_J2,espacio3_J2=Seleccion_Hechizos(usuario1,usuario2,turno,espacio1_J1,espacio2_J1,espacio3_J1,espacio1_J2,espacio2_J2,espacio3_J2)
			
			# Asignando Espacio a Hechizos
			# Jugador 1 Hechizo 1
			if espacio1_J1 == 1: espacio1_J1 = hechizo1 
			elif espacio2_J1 == 1: espacio2_J1 = hechizo1 
			elif espacio3_J1 == 1: espacio3_J1 = hechizo1
			# Jugador 2 Hechizo 1
			elif espacio1_J2 == 1: espacio1_J2 = hechizo1 
			elif espacio2_J2 == 1: espacio2_J2 = hechizo1 
			elif espacio3_J2 == 1: espacio3_J2 = hechizo1
			
			# Jugador 1 Hechizo 2
			if espacio1_J1 == 2: espacio1_J1 = hechizo2
			elif espacio2_J1 == 2: espacio2_J1 = hechizo2
			elif espacio3_J1 == 2: espacio3_J1 = hechizo2
			# Jugador 2 Hechizo 2
			elif espacio1_J2 == 2: espacio1_J2 = hechizo2
			elif espacio2_J2 == 2: espacio2_J2 = hechizo2
			elif espacio3_J2 == 2: espacio3_J2 = hechizo2
			
			# Jugador 1 Hechizo 3
			if espacio1_J1 == 3: espacio1_J1 = hechizo3
			elif espacio2_J1 == 3: espacio2_J1 = hechizo3
			elif espacio3_J1 == 3: espacio3_J1 = hechizo3
			# Jugador 2 Hechizo 3
			elif espacio1_J2 == 3: espacio1_J2 = hechizo3
			elif espacio2_J2 == 3: espacio2_J2 = hechizo3
			elif espacio3_J2 == 3: espacio3_J2 = hechizo3

			# Jugador 1 Hechizo 4
			if espacio1_J1 == 4: espacio1_J1 = hechizo4
			elif espacio2_J1 == 4: espacio2_J1 = hechizo4
			elif espacio3_J1 == 4: espacio3_J1 = hechizo4
			# Jugador 2 Hechizo 4
			elif espacio1_J2 == 4: espacio1_J2 = hechizo4
			elif espacio2_J2 == 4: espacio2_J2 = hechizo4
			elif espacio3_J2 == 4: espacio3_J2 = hechizo4

			# Jugador 1 Hechizo 5
			if espacio1_J1 == 5: espacio1_J1 = hechizo5
			elif espacio2_J1 == 5: espacio2_J1 = hechizo5
			elif espacio3_J1 == 5: espacio3_J1 = hechizo5
			# Jugador 2 Hechizo 5
			elif espacio1_J2 == 5: espacio1_J2 = hechizo5
			elif espacio2_J2 == 5: espacio2_J2 = hechizo5
			elif espacio3_J2 == 5: espacio3_J2 = hechizo5

			# Jugador 1 Hechizo 3
			if espacio1_J1 == 6: espacio1_J1 = hechizo6
			elif espacio2_J1 == 6: espacio2_J1 = hechizo6
			elif espacio3_J1 == 6: espacio3_J1 = hechizo6
			# Jugador 2 Hechizo 6
			elif espacio1_J2 == 6: espacio1_J2 = hechizo6
			elif espacio2_J2 == 6: espacio2_J2 = hechizo6
			elif espacio3_J2 == 6: espacio3_J2 = hechizo6


			while combate == True:
				while turno == 1:
					os.system(borrar)
					print("Turno de: ",usuario1,"    HP: ", hp1,"    Tu Energía: ",energia1,"    ",usuario2,": ",hp2)
					print("Seleccione Ataque")
					print("1 - Ataque Bàsico = -5HP   Energia: 1")
					print("2 - Ataque Medio  = -15HP  Energia: 2")
					print("3 - Ataque Fuerte = -25HP  Energia: 3")
					# Posición 4:
					if espacio1_J1 == hechizo1: print("4 - Destrucciòn Masiva = -100HP   Energia: 8")
					elif espacio1_J1 == hechizo2: print("4 - Magos = -30HP   Energia: 2")
					elif espacio1_J1 == hechizo3: print("4 - Virus y Sabotage = -75HP   Energia: 8")
					elif espacio1_J1 == hechizo4: print("4 - Robo de Energía   Energia: 9")
					elif espacio1_J1 == hechizo5: print("4 - Robo de Ruleta   Energia: 12")
					elif espacio1_J1 == hechizo6: print("4 - bola de Fuego = -50HP   Energia: 4")
					# Posición 5:
					if espacio2_J1 == hechizo1: print("5 - Destrucciòn Masiva = -100HP   Energia: 8")
					elif espacio2_J1 == hechizo2: print("5 - Magos = -30HP   Energia: 2")
					elif espacio2_J1 == hechizo3: print("5 - Virus y Sabotage = -75HP   Energia: 8")
					elif espacio2_J1 == hechizo4: print("5 - Robo de Energía   Energia: 9")
					elif espacio2_J1 == hechizo5: print("5 - Robo de Ruleta   Energia: 12")
					elif espacio2_J1 == hechizo6: print("5 - bola de Fuego = -50HP   Energia: 4")
					# Posición 6:
					if espacio3_J1 == hechizo1: print("6 - Destrucciòn Masiva = -100HP   Energia: 8")
					elif espacio3_J1 == hechizo2: print("6 - Magos = -30HP   Energia: 2")
					elif espacio3_J1 == hechizo3: print("6 - Virus y Sabotage = -75HP   Energia: 8")
					elif espacio3_J1 == hechizo4: print("6 - Robo de Energía   Energia: 9")
					elif espacio3_J1 == hechizo5: print("6 - Robo de Ruleta   Energia: 12")
					elif espacio3_J1 == hechizo6: print("6 - bola de Fuego = -50HP   Energia: 4")
					print("7 - Ruleta: ", ruleta1, "   Energia: 5")
					print("8 - Cargar")
					print()
					ataque = int(input("->"))

					if ataque == 1 and energia1 >= 1: hp2 -= ataque_basico; energia1 -= 1
					elif ataque == 2 and energia1 >= 2: hp2 -= ataque_medio; energia1 -= 2
					elif ataque == 3 and energia1 >= 3: hp2 -= ataque_fuerte; energia1 -= 3
					# Posición 4
					elif ataque == 4 and espacio1_J1 == hechizo1 and energia1 >= 8:
						hp2 -= espacio1_J1; energia1 -=8
					elif ataque == 4 and espacio1_J1 == hechizo2 and energia1 >= 2:
						hp2 -= espacio1_J1; energia1 -= 2
					elif ataque == 4 and espacio1_J1 == hechizo3 and energia1 >= 8:
						hp2 -= espacio1_J1; energia1 -= 8
					elif ataque == 4 and espacio1_J1 == hechizo4 and energia1 >= 9:
						energia1 += energia2; energia2 = 1; energia1 -= 9
					elif ataque == 4 and espacio1_J1 == hechizo5 and energia1 >= 12:
						ruleta1 += ruleta2; ruleta2 = 0; energia1 -= 12
					elif ataque == 4 and espacio1_J1 == hechizo6 and energia1 >= 4:
						hp2 -= espacio1_J1; energia1 -= 4
					# Posición 5
					elif ataque == 5 and espacio2_J1 == hechizo1 and energia1 >= 8:
						hp2 -= espacio2_J1; energia1 -=8
					elif ataque == 5 and espacio2_J1 == hechizo2 and energia1 >= 2:
						hp2 -= espacio2_J1; energia1 -= 2
					elif ataque == 5 and espacio2_J1 == hechizo3 and energia1 >= 8:
						hp2 -= espacio2_J1; energia1 -= 8
					elif ataque == 5 and espacio2_J1 == hechizo4 and energia1 >= 9:
						energia1 += energia2; energia2 = 1; energia1 -= 9
					elif ataque == 5 and espacio2_J1 == hechizo5 and energia1 >= 12:
						ruleta1 += ruleta2; ruleta2 = 0; energia1 -= 12
					elif ataque == 5 and espacio2_J1 == hechizo6 and energia1 >= 4:
						hp2 -= espacio2_J1; energia1 -= 4
					# Posición 6
					elif ataque == 6 and espacio3_J1 == hechizo1 and energia1 >= 8:
						hp2 -= espacio3_J1; energia1 -=8
					elif ataque == 6 and espacio3_J1 == hechizo2 and energia1 >= 2:
						hp2 -= espacio3_J1; energia1 -= 2
					elif ataque == 6 and espacio3_J1 == hechizo3 and energia1 >= 8:
						hp2 -= espacio3_J1; energia1 -= 8
					elif ataque == 6 and espacio3_J1 == hechizo4 and energia1 >= 9:
						energia1 += energia2; energia2 = 1; energia1 -= 9
					elif ataque == 6 and espacio3_J1 == hechizo5 and energia1 >= 12:
						ruleta1 += ruleta2; ruleta2 = 0; energia1 -= 12
					elif ataque == 6 and espacio3_J1 == hechizo6 and energia1 >= 4:
						hp2 -= espacio3_J1; energia1 -= 4

					elif ataque == 7 and ruleta1 > 0 and energia1 >= 5:
						ruleta1 -= 1; energia1 -= 5


					elif ataque == 8:
						energia1 += 1
						turno = 2

				while turno == 2:
					os.system(borrar)
					print("Turno de: ",usuario2,"    HP: ", hp2,"    Tu Energía: ",energia2,"    ",usuario1,": ",hp1)
					print("Seleccione Ataque")
					print("1 - Ataque Bàsico = -5HP   Energia: 1")
					print("2 - Ataque Medio  = -15HP  Energia: 2")
					print("3 - Ataque Fuerte = -25HP  Energia: 3")
					# Posición 4:
					if espacio1_J2 == hechizo1: print("4 - Destrucciòn Masiva = -100HP   Energia: 8")
					elif espacio1_J2 == hechizo2: print("4 - Magos = -30HP   Energia: 2")
					elif espacio1_J2 == hechizo3: print("4 - Virus y Sabotage = -75HP   Energia: 8")
					elif espacio1_J2 == hechizo4: print("4 - Robo de Energía   Energia: 9")
					elif espacio1_J2 == hechizo5: print("4 - Robo de Ruleta   Energia: 12")
					elif espacio1_J2 == hechizo6: print("4 - bola de Fuego = -50HP   Energia: 4")
					# Posición 5:
					if espacio2_J2 == hechizo1: print("5 - Destrucciòn Masiva = -100HP   Energia: 8")
					elif espacio2_J2 == hechizo2: print("5 - Magos = -30HP   Energia: 2")
					elif espacio2_J2 == hechizo3: print("5 - Virus y Sabotage = -75HP   Energia: 8")
					elif espacio2_J2 == hechizo4: print("5 - Robo de Energía   Energia: 9")
					elif espacio2_J2 == hechizo5: print("5 - Robo de Ruleta   Energia: 12")
					elif espacio2_J2 == hechizo6: print("5 - bola de Fuego = -50HP   Energia: 4")
					# Posición 6:
					if espacio3_J2 == hechizo1: print("6 - Destrucciòn Masiva = -100HP   Energia: 8")
					elif espacio3_J2 == hechizo2: print("6 - Magos = -30HP   Energia: 2")
					elif espacio3_J2 == hechizo3: print("6 - Virus y Sabotage = -75HP   Energia: 8")
					elif espacio3_J2 == hechizo4: print("6 - Robo de Energía   Energia: 9")
					elif espacio3_J2 == hechizo5: print("6 - Robo de Ruleta   Energia: 12")
					elif espacio3_J2 == hechizo6: print("6 - bola de Fuego = -50HP   Energia: 4")
					print("7 - Ruletas: ",ruleta2,"   Energia: 5")
					print("8 - Cargar")
					
					print()
					ataque = int(input("->"))

					if ataque == 1 and energia2 >= 1: hp1 -= ataque_basico; energia2 -= 1
					elif ataque == 2 and energia2 >= 2: hp1 -= ataque_medio; energia2 -= 2
					elif ataque == 3 and energia2 >= 3: hp1 -= ataque_fuerte; energia2 -= 3
					# Posición 4
					elif ataque == 4 and espacio1_J2 == hechizo1 and energia2 >= 8:
						hp1 -= espacio1_J2; energia2 -=8
					elif ataque == 4 and espacio1_J2 == hechizo2 and energia2 >= 2:
						hp1 -= espacio1_J2; energia2 -= 2
					elif ataque == 4 and espacio1_J2 == hechizo3 and energia2 >= 8:
						hp1 -= espacio1_J2; energia2 -= 8
					elif ataque == 4 and espacio1_J2 == hechizo4 and energia2 >= 9:
						energia2 += energia1; energia1 = 1; energia2 -= 9
					elif ataque == 4 and espacio1_J2 == hechizo5 and energia2 >= 12:
						ruleta2 += ruleta1; ruleta1 = 0; energia2 -= 12
					elif ataque == 4 and espacio1_J2 == hechizo6 and energia2 >= 4:
						hp1 -= espacio1_J2; energia2 -= 4
					# Posición 5
					elif ataque == 5 and espacio2_J2 == hechizo1 and energia2 >= 8:
						hp1 -= espacio2_J2; energia2 -=8
					elif ataque == 5 and espacio2_J2 == hechizo2 and energia2 >= 2:
						hp1 -= espacio2_J2; energia2 -= 2
					elif ataque == 5 and espacio2_J2 == hechizo3 and energia2 >= 8:
						hp1 -= espacio2_J2; energia2 -= 8
					elif ataque == 5 and espacio2_J2 == hechizo4 and energia2 >= 9:
						energia2 += energia1; energia1 = 1; energia2 -= 9
					elif ataque == 5 and espacio2_J2 == hechizo5 and energia2 >= 12:
						ruleta2 += ruleta1; ruleta1 = 0; energia2 -= 12
					elif ataque == 5 and espacio2_J2 == hechizo6 and energia2 >= 4:
						hp1 -= espacio2_J2; energia2 -= 4
					# Posición 6
					elif ataque == 6 and espacio3_J2 == hechizo1 and energia2 >= 8:
						hp1 -= espacio3_J2; energia2 -=8
					elif ataque == 6 and espacio3_J2 == hechizo2 and energia2 >= 2:
						hp1 -= espacio3_J2; energia2 -= 2
					elif ataque == 6 and espacio3_J2 == hechizo3 and energia2 >= 8:
						hp1 -= espacio3_J2; energia2 -= 8
					elif ataque == 6 and espacio3_J2 == hechizo4 and energia2 >= 9:
						energia2 += energia1; energia1 = 1; energia2 -= 9
					elif ataque == 6 and espacio3_J2 == hechizo5 and energia2 >= 12:
						ruleta2 += ruleta1; ruleta1 = 0; energia2 -= 12
					elif ataque == 6 and espacio3_J2 == hechizo6 and energia2 >= 4:
						hp1 -= espacio3_J2; energia2 -= 4

					elif ataque == 7 and ruleta2 > 0:
						ruleta2 -= 1

					
					elif ataque == 8:
						energia2 += 1
						turno = 1
	#-------------------------------------------------------------------------------------------------------
		elif seleccion == 2:
			break

def Seleccion_Hechizos(usuario1, usuario2, turno, espacio1_J1, espacio2_J1, espacio3_J1, espacio1_J2, espacio2_J2, espacio3_J2):

	# Variables Locales
	ronda_J1 = 0; ronda_J2 = 0; hechizos = 0; borrar = 'cls'
	dado = 1,2,3,4,5,6; dado2 = 1,2,3,4,5,6; tiempo = 3

	# Lanzar Dado
	while True:
		os.system(borrar)
		print(" Selección de Habilidades")
		print(" Lanza el Dado ",usuario1,": ENTER")
		input()
		numero = random.choice(dado)
	
		os.system(borrar)
		print(" Selección de Habilidades")
		print(" Dado de ",usuario1,": ",numero)
		print(" Lanza el Dado ",usuario2,": ENTER")
		input()
		numero2 = random.choice(dado2)
		os.system(borrar)
		print(" Selección de Habilidades")
		print(" Dado de ",usuario1,": ",numero)
		print(" Dado de ",usuario2,": ",numero2)

		if numero == numero2:
			print(" Empate: Deben volver a lanzar")
			time.sleep(tiempo)
		elif numero > numero2:
			turno = 1
			print(usuario1, " Escoge Primero")
			time.sleep(tiempo)
			break
		else:
			turno = 2
			print(usuario2, " Escoge Primero")
			time.sleep(tiempo)
			break
	
	while True:
		if turno == 1:
			os.system(borrar)
			print(usuario1, " Elija un Hechizos")
			print("Lista de Hechizos")
			print("    |       Nombre       |     Utilizadad     |   Consumo   |")
			# Hechizo 1
			if espacio1_J1 != 1 and espacio2_J1 != 1 and espacio3_J1 != 1 and espacio1_J2 != 1 and espacio2_J2 != 1 and espacio3_J2 != 1:
				print("1 - | Destrucciòn Masiva |       -100HP       |  Energia: 8 |")
			# Hechizo 2
			if espacio1_J1 != 2 and espacio2_J1 != 2 and espacio3_J1 != 2 and espacio1_J2 != 2 and espacio2_J2 != 2 and espacio3_J2 != 2:
				print("2 - |       Magos        |  -30HP (5 Turnos)  |  Energia: 2 |")
			# Hechizo 3
			if espacio1_J1 != 3 and espacio2_J1 != 3 and espacio3_J1 != 3 and espacio1_J2 != 3 and espacio2_J2 != 3 and espacio3_J2 != 3:
				print("3 - |  Virus y Sabotage  |       -75HP        |  Energia: 8 |")
			# Hechizo 4
			if espacio1_J1 != 4 and espacio2_J1 != 4 and espacio3_J1 != 4 and espacio1_J2 != 4 and espacio2_J2 != 4 and espacio3_J2 != 4:
				print("4 - |  Robo de Energìa   |    Roba Energia    |  Energia: 9 |")
			# Hechizo 5
			if espacio1_J1 != 5 and espacio2_J1 != 5 and espacio3_J1 != 5 and espacio1_J2 != 5 and espacio2_J2 != 5 and espacio3_J2 != 5:
				print("5 - |  Robo de Ruletas   |    Roba Ruletas    |  Energia: 12|")
			# Hechizo 6
			if espacio1_J1 != 6 and espacio2_J1 != 6 and espacio3_J1 != 6 and espacio1_J2 != 6 and espacio2_J2 != 6 and espacio3_J2 != 6:
				print("6 - |  Bola de Fuergo    |  -50HP (6 Turnos)  |  Energia: 3 |")

			if ronda_J1 == 0:
				espacio1_J1 = int(input("-> "))
			elif ronda_J1 == 1:
				espacio2_J1 = int(input("-> "))
			elif ronda_J1 == 2:
				espacio3_J1 = int(input("-> "))
			
			ronda_J1 += 1
			turno = 2
			hechizos += 1

			if hechizos == 6 and espacio3_J1 != 0 and espacio3_J2 != 0:
				break

		elif turno == 2:
			os.system(borrar)
			print(usuario2, " Elija un Hechizos")
			print("Lista de Hechizos")
			print("    |       Nombre       |     Utilizadad     |   Consumo   |")
			# Hechizo 1
			if espacio1_J1 != 1 and espacio2_J1 != 1 and espacio3_J1 != 1 and espacio1_J2 != 1 and espacio2_J2 != 1 and espacio3_J2 != 1:
				print("1 - | Destrucciòn Masiva |       -100HP       |  Energia: 8 |")
			# Hechizo 2
			if espacio1_J1 != 2 and espacio2_J1 != 2 and espacio3_J1 != 2 and espacio1_J2 != 2 and espacio2_J2 != 2 and espacio3_J2 != 2:
				print("2 - |       Magos        |  -30HP (5 Turnos)  |  Energia: 2 |")
			# Hechizo 3
			if espacio1_J1 != 3 and espacio2_J1 != 3 and espacio3_J1 != 3 and espacio1_J2 != 3 and espacio2_J2 != 3 and espacio3_J2 != 3:
				print("3 - |  Virus y Sabotage  |       -75HP        |  Energia: 8 |")
			# Hechizo 4
			if espacio1_J1 != 4 and espacio2_J1 != 4 and espacio3_J1 != 4 and espacio1_J2 != 4 and espacio2_J2 != 4 and espacio3_J2 != 4:
				print("4 - |  Robo de Energìa   |    Roba Energia    |  Energia: 9 |")
			# Hechizo 5
			if espacio1_J1 != 5 and espacio2_J1 != 5 and espacio3_J1 != 5 and espacio1_J2 != 5 and espacio2_J2 != 5 and espacio3_J2 != 5:
				print("5 - |  Robo de Ruletas   |    Roba Ruletas    |  Energia: 12|")
			# Hechizo 6
			if espacio1_J1 != 6 and espacio2_J1 != 6 and espacio3_J1 != 6 and espacio1_J2 != 6 and espacio2_J2 != 6 and espacio3_J2 != 6:
				print("6 - |  Bola de Fuergo    |  -50HP (6 Turnos)  |  Energia: 3 |")


			if ronda_J2 == 0:
				espacio1_J2 = int(input("-> "))
			elif ronda_J2 == 1:
				espacio2_J2 = int(input("-> "))
			elif ronda_J2 == 2:
				espacio3_J2 = int(input("-> "))
			
			ronda_J2 += 1
			turno = 1
			hechizos += 1

		if hechizos == 6 and espacio3_J1 != 0 and espacio3_J2 != 0:
			break

	return usuario1, usuario2, turno, espacio1_J1, espacio2_J1, espacio3_J1, espacio1_J2, espacio2_J2, espacio3_J2


def Ruleta():
	pass


"""
---------------------------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------------------------

Inicio del Programa Aquí              Inicio del Programa Aquí             Inicio del Programa Aquí          Inicio del Programa Aquí

---------------------------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------------------------
"""

# Declaración e Iniciación de Variables
borrar = "cls"; usuario = ""
#------------------------------------------
inicio1 = False
#------------------------------------------
hp = 0; select = 0
#------------------------------------------

# Objeto de Errores
errores = Errores()

while True:
	os.system(borrar)
	try:
		print()
		print("      ************************************")
		print("      *                                  *")
		print("      *         Ârea de Registro         *")
		print("      *                                  *")
		print("      ************************************")
		seleccion = int(input("""

   1 - Iniciar Sesion 
   2 - Registro

-> """))

		if seleccion == 1:
			usuario, hp, inicio1 = Inicio_Sesion(usuario, hp, inicio1)
			if inicio1 == True:
				break
		elif seleccion == 2:
			usuario, hp, inicio1 = Registro(usuario, hp, inicio1)
			if inicio1 == True:
				break
		else:
			errores.Error2()

	except ValueError:
		errores.Error1()


# Inicio del Juego
if inicio1 == True:
	while inicio1 == True:
		select = MenuSeleccion(select)

		if select == 1:
			Modo_De_Juego_1(usuario,hp)

		if select == 6:
			inicio1 = False
			os.system(borrar)

