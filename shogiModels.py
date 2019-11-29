"""
Nombre: Andres Convertini
Juego: Shogi
Año: 2019
V02:
	# Añade la funcionalidad de permitir un movimiento erroneo
	# Verifica que piezas hay al momento de querer ingresar la pieza
"""

import os

# IMPORTAMOS LOS MODELOS DE LAS PIEZAS
from piezas.pieza import *
from piezas.rey import Rey
from piezas.generalOro import generalOro
from piezas.generalPlata import generalPlata
from piezas.caballo import Caballo
from piezas.lancero import Lancero
from piezas.torre import Torre
from piezas.alfil import Alfil
from piezas.peon import Peon

# IMPORTAMOS EL MODELO DE JUGADOR
from jugadores.jugador import Jugador
from check import _buscarRey

JUGADOR_BLANCO = ""
JUGADOR_NEGRO = ""

endGame = False


def mostrarMensaje(Jugador):

	print(Jugador.mensaje())


# Función para crear un array de 9x9 que será luego el tablero
def crearArrayTablero():

	tablero = ["  "]*9

	for i in range(0,9):
		tablero[i] = ["  "]*9

	# Creamos y colocamos las piezas
	for i in range(0,9):
		for j in range(0,9):

			"""Cada elemento tablero[i][j] es un objeto del tipo pieza de cada una"""
			"""
			i son las filas ===> x
			j son las columnas ===> y
			"""
			# if(i == 2 and j !=0): # Peón blanco
			# 	peon = Peon('blanco', 'negro', i, j)
			# 	tablero[i][j] = peon
			# elif(i == 5 and j == 0):
			# 	peon = Peon('blanco', 'negro', i, j)
			# 	tablero[i][j] = peon
			if(i == 2): # Peón blanco
				peon = Peon('blanco', 'negro', i, j)
				tablero[i][j] = peon				
			elif(i == 6): # Peón negro
				peon = Peon('negro', 'blanco', i, j)
				tablero[i][j] = peon
			elif(i == 1 and j == 1): # Torre Blanca
				torre = Torre('blanco', 'negro', i, j)
				tablero[i][j] = torre
			elif(i == 7 and j == 7): # Torre Negra
				torre = Torre('negro', 'blanco', i, j)
				tablero[i][j] = torre
			elif(i == 1 and j == 7): # Alfil Blanco
				alfil = Alfil('blanco', 'negro', i, j)
				tablero[i][j] = alfil
			elif(i == 7 and j == 1): # Alfil Negro
				alfil = Alfil('negro', 'blanco', i, j)
				tablero[i][j] = alfil
			elif(i == 0 and (j == 0 or j == 8)): # Lancero Blanco
				lancero = Lancero('blanco', 'negro', i, j)
				tablero[i][j] = lancero
			elif(i == 8 and (j == 0 or j == 8)): # Lancero Negro
				lancero = Lancero('negro', 'blanco', i, j)
				tablero[i][j] = lancero
			elif(i == 0 and (j == 1 or j == 7)): # Caballo Blanco
				caballo = Caballo('blanco', 'negro', i, j)
				tablero[i][j] = caballo
			elif(i == 8 and (j == 1 or j == 7)): # Caballo Negro
				caballo = Caballo('negro', 'blanco', i, j)
				tablero[i][j] = caballo
			elif(i == 0 and (j == 2 or j == 6)): # General Plata Blanco
				plata = generalPlata('blanco', 'negro', i, j)
				tablero[i][j] = plata
			elif(i == 8 and (j == 2 or j == 6)): # General Plata Negro
				plata = generalPlata('negro', 'blanco', i, j)
				tablero[i][j] = plata
			elif(i == 0 and (j == 3 or j == 5)): # General Oro Blanco
				oro = generalOro('blanco', 'negro', i, j)
				tablero[i][j] = oro
			elif(i == 8 and (j == 3 or j == 5)): # General Oro Negro
				oro = generalOro('negro', 'blanco', i, j)
				tablero[i][j] = oro
			elif(i == 0 and j == 4): # Rey Blanco
				rey = Rey('blanco', 'negro', i, j)
				tablero[i][j] = rey
			elif(i == 8 and j == 4): # Rey Negro
				rey = Rey('negro', 'blanco', i, j)
				tablero[i][j] = rey


	return tablero

# Función que imprime el tablero en la pantalla.
def imprimirTablero(tablero):

	print("     0      1      2      3      4      5      6      7      8")
	for i in range(0,9):
		line = '{} |'.format(i)
		for j in range(0,9):
			line += " {}    ".format(str(tablero[i][j]))
		print(line+'\n')

# Función que imprime el encabezado de cada jugador
def imprimirEncabezado(jugador, tablero):

	# Turno para el jugador blanco/negro
	print("Turno del jugador {}. Movimiento nro: {}".format(jugador.__dict__['equipo'], jugador.__dict__['movimiento']))
	print("========================================================="+"\n")

	# Método que debe ejecutarse cada vez que termine un turno.
	imprimirTablero(tablero)

	print("\n"+"=========================================================")
	print("Piezas capturadas")

	piezas_capturadas = {}
	j = 0
	for i in jugador.__dict__['PIEZAS_CAPTURADAS']:  
		piezas_capturadas[j] = (i.__dict__['descriptor'])
		j = j + 1
	print(piezas_capturadas)
	# for i in range(0, int(len(jugador.__dict__['PIEZAS_CAPTURADAS']))):
	# 	print(str(i)+" ")

	print("\n\n"+"===========================================================")

# Función que solicita los movimientos de las piezas
def moverPieza(tablero, jugador):

	# buscamos el rey enemigo
	_buscarRey(tablero, jugador)

	# Variable para evaluar si el movimiento es válido
	movimientoJugadorValido = False
	# Variable para contar intentos de movimientos erróneos
	contadorMovimientoInvalido = 0

	while (movimientoJugadorValido == False and contadorMovimientoInvalido != 2):


		desicion = 0
		if(int(len(jugador.__dict__['PIEZAS_CAPTURADAS'])) > 0):
			try:
				desicion = int(input('Desea ingresar una pieza o realizar un movimiento (1 o 2) \n'))
			except Exception:
				print('VALOR INCORRECTO')
				desicion = int(input('Desea ingresar una pieza o realizar un movimiento (1 o 2) \n'))
		if(desicion == 0 or desicion == 2):

			while True:
				# No salimos del bucle hasta que elijamos una pieza correcta
				rowColumn = input("Ingrese pieza a mover fila y columna separadas por espacio \n")
				
				columna1 = int(rowColumn[2])
				fila1 = int(rowColumn[0])

				# Capturamos la pieza
				piezaSeleccionada = tablero[fila1][columna1]

				try:
					if(piezaSeleccionada.team == jugador.equipo):
						break
					else:
						print('Debe seleccionar una pieza válida')
						continue
				except Exception:
					print('Debe seleccionar una pieza válida')
					continue									
					

			newRowColumn = input('Ingrese lugar nueva posición (fila, columna) de la pieza separadas por espacio \n')

			columna2 = int(newRowColumn[2])
			fila2 = int(newRowColumn[0])


			# Deberíamos pasar esto al método que realiza el movimiento para ver si efectivamente es válido el movimiento
			movimientoX = fila2 - fila1
			movimientoY = columna2 - columna1

			# Validamos si el movimiento es válido en función de la pieza
			if(tablero[fila2][columna2] == "  " or tablero[fila2][columna2] == " "):
				# No hay ninguna pieza en la posición a desplazar

				if(tipoPieza(movimientoY, movimientoX, piezaSeleccionada, False, None ) == True):
					# Significa que el movimiento fué válido, entonces ejecutamos el movimiento
					tablero[fila1][columna1] = "  "
					# Cambiamos la posición de la pieza
					piezaSeleccionada.posicionX = fila2
					piezaSeleccionada.posicionY = columna2

					# Evaluamos si la pieza es coronada o no
					# Por razones de sencillez, coronamos al llegar a la fila 2 0 6, sin dar opción al jugador (en una primera instancia)
					piezaSeleccionada.coronar()

					# Le asignamos a la casilla del tablero la pieza correspondiente
					tablero[fila2][columna2] = piezaSeleccionada

					movimientoJugadorValido == True
					return True
				else:
					os.system('cls')
					print("MOVIMIENTO INVÁLIDO. UN INTENTO RESTANTE")
					# Reimprimimos el tablero de nuevo
					imprimirEncabezado(jugador, tablero)
					# Cargamos el contador con + 1
					contadorMovimientoInvalido = contadorMovimientoInvalido + 1
					if(contadorMovimientoInvalido > 1):
						return False
					else:
						continue
			else:

				# Hay una pieza en el lugar donde queremos movernos
				if(tipoPieza(movimientoY, movimientoX, piezaSeleccionada, True, tablero[fila2][columna2])):
					# Significa que el movimiento fué válido, entonces ejecutamos el movimiento
					jugador.__dict__['PIEZAS_CAPTURADAS'].append(tablero[fila2][columna2])
					# Capturamos la pieza y la guardamos en el array de piezas capturadas del jugador que corresponde
					tablero[fila1][columna1] = "  "
					# Cambiamos la posición de la pieza
					piezaSeleccionada.posicionX = fila2
					piezaSeleccionada.posicionY = columna2

					# Evaluamos si la pieza es coronada o no
					# Por razones de sencillez, coronamos al llegar a la fila 2 0 6, sin dar opción al jugador (en una primera instancia)
					piezaSeleccionada.coronar()

					# Le asignamos a la casilla del tablero la pieza correspondiente
					tablero[fila2][columna2] = piezaSeleccionada

					movimientoJugadorValido = True
					return True
				else:
					os.system('cls')
					print("MOVIMIENTO INVÁLIDO. UN INTENTO RESTANTE")
					# Reimprimimos el tablero de nuevo
					imprimirEncabezado(jugador, tablero)
					# Cargamos el contador con + 1
					contadorMovimientoInvalido = contadorMovimientoInvalido + 1
					if(contadorMovimientoInvalido > 1):
						return False
					else:
						continue

		elif(desicion == 1):
			# print('desicion1')

			respuesta = jugador.introducirPieza(jugador, tablero)
			if(respuesta == False):
				os.system('cls')
				print("MOVIMIENTO INVÁLIDO. UN INTENTO RESTANTE")
				# Reimprimimos el tablero de nuevo
				imprimirEncabezado(jugador, tablero)
				# Cargamos el contador con + 1
				contadorMovimientoInvalido = contadorMovimientoInvalido + 1
				if(contadorMovimientoInvalido > 1):
					return False
				else:
					continue				
			elif(respuesta != False):
				movimientoJugadorValido = True
				return respuesta

		
# Función que ejecuta el movimiento de la pieza en función del tipo de pieza
def tipoPieza(x, y, pieza, vacio, PiezaAtacada):
	# Pieza trae la pieza a mover
	# PiezaAtacada nos dice si en la nueva posición del tablero hay una pieza.
	# Equipo viene de la pieza a mover
	equipo = pieza.__dict__['team']
	if(equipo == 'negro'):
		multiplicadorY = -1
	else:
		multiplicadorY = 1

	if(PiezaAtacada != None):
		colorPiezaAtacada = PiezaAtacada.__dict__['team']
	else:
		colorPiezaAtacada = None

	# Vacío en caso de que el lugar se encuentre vacío. Es booleano. En caso de que el lugar no este ocupado vacio es igual a false
	# PiezaAtacada, solo en caso de que estemos yendo a una ubicación con una pieza. 
	if(str(pieza.__dict__['tipo']) == 'Peón'):
		# x, y, pieza, equipo, colorPiezaEnemiga
		movimiento = Peon.movimiento(x, (multiplicadorY * y), vacio, equipo, colorPiezaAtacada, pieza)
		return movimiento
	elif(str(pieza.__dict__['tipo']) == 'GeneralOro'):
		movimiento = generalOro.movimiento(x, (multiplicadorY * y), vacio, equipo, colorPiezaAtacada, pieza)
		return movimiento
	elif(str(pieza.__dict__['tipo']) == 'Lancero'):
		movimiento = Lancero.movimiento(x, (multiplicadorY * y), vacio, equipo, colorPiezaAtacada, pieza)
		return movimiento
	elif(str(pieza.__dict__['tipo']) == 'Caballo'):
		movimiento = Caballo.movimiento(x, (multiplicadorY * y), vacio, equipo, colorPiezaAtacada, pieza)
		return movimiento
	elif(str(pieza.__dict__['tipo']) == 'GeneralPlata'):
		movimiento = generalPlata.movimiento(x, (multiplicadorY * y), vacio, equipo, colorPiezaAtacada, pieza)
		return movimiento
	elif(str(pieza.__dict__['tipo']) == 'Rey'):
		movimiento = Rey.movimiento(x, (multiplicadorY * y), vacio, equipo, colorPiezaAtacada, pieza)
		return movimiento
	elif(str(pieza.__dict__['tipo']) == 'Alfil'):
		movimiento = Alfil.movimiento(x, (multiplicadorY * y), vacio, equipo, colorPiezaAtacada, pieza)
		return movimiento
	elif(str(pieza.__dict__['tipo']) == 'Torre'):
		movimiento = Torre.movimiento(x, (multiplicadorY * y), vacio, equipo, colorPiezaAtacada, pieza)
		return movimiento









# INICIAMOS EL JUEGO

def main():

	# Creamos los jugador por primera ves
	JUGADOR_BLANCO = Jugador('blanco', 'negro')
	JUGADOR_NEGRO = Jugador('negro', 'blanco')
	# Iniciamos los turnos a 0
	TURNO_BLANCO = 0
	TURNO_NEGRO = 0

	# MATRIZ 2X2 QUE CONTIENE TODAS LAS PIEZAS UBICADAS
	tablero = crearArrayTablero()

	while endGame == False:

		# Limpiamos la consola
		os.system('cls')

		print("========================================================="+"\n")


		# Mostamos mensaje del turno
		if(TURNO_NEGRO == TURNO_BLANCO):
			# Juega blanco primero

			# Imprimimos encabezado común para ambos jugadores
			imprimirEncabezado(JUGADOR_BLANCO, tablero)

			# Si el jugador elije mover pieza, ejecutamos la función que se encarga de ello. Le debemos pasar por parámetros tanto el tablero como el jugador
			movimiento = moverPieza(tablero, JUGADOR_BLANCO)
			if(movimiento == True or movimiento == False):

				TURNO_BLANCO = TURNO_BLANCO + 1
				JUGADOR_BLANCO.movimiento = int(TURNO_BLANCO)
			elif(movimiento != False and movimiento != True):
				# En la espuesta viene el nuevo tablero
				tablero = movimiento
				TURNO_BLANCO = TURNO_BLANCO + 1
				JUGADOR_BLANCO.movimiento = int(TURNO_BLANCO)

			input('Presione intro para finalizar el turno')

		elif(TURNO_NEGRO < TURNO_BLANCO):
			# Juega negro

			# Imprimimos encabezado común para ambos jugadores
			imprimirEncabezado(JUGADOR_NEGRO, tablero)

			# Si el jugador elije mover pieza, ejecutamos la función que se encarga de ello. Le debemos pasar por parámetros tanto el tablero como el jugador
			movimiento = moverPieza(tablero, JUGADOR_NEGRO)
			if(movimiento == True):

				TURNO_NEGRO = TURNO_NEGRO + 1
				JUGADOR_NEGRO.movimiento = int(TURNO_NEGRO)
			elif(movimiento != False and movimiento != True):
				tablero = movimiento
				TURNO_NEGRO = TURNO_NEGRO + 1
				JUGADOR_NEGRO.movimiento = int(TURNO_NEGRO)

			input('Presione intro para finalizar el turno')


		

if __name__ == '__main__':
 main()






	






























