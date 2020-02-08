from variables import *
import time
import os

def Error1():
	os.system(color_error)
	print()
	print(" -> No ha seleccionado ninguna opción")
	time.sleep(tiempo_error)
	os.system(color_inicio)

def Error2():
	os.system(color_error)
	print()
	print(" -> Solo se aceptan valores Numericos")
	time.sleep(tiempo_error)
	os.system(color_inicio)