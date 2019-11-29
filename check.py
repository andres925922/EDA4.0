from piezas.pieza import *
from piezas.rey import Rey
from piezas.generalOro import generalOro
from piezas.generalPlata import generalPlata
from piezas.caballo import Caballo
from piezas.lancero import Lancero
from piezas.torre import Torre
from piezas.alfil import Alfil
from piezas.peon import Peon

def _buscarRey(tablero, jugador):
	for i in range(0,9):
		for j in range(0,9):
			# Verificamos que la casilla no este vacía
			if(tablero[i][j] != "  "):
				# Verificamos que la pieza sea un rey y sea enemigo (turno oponente)
				if(tablero[i][j].__dict__['team'] != jugador.__dict__['equipo'] and tablero[i][j].__dict__['tipo'] == 'Rey'):
					# Ejecutamos los métodos que evalúan si se puede mover el rey
					rey = tablero[i][j]
					ubicacionesDisponiblesRey(rey, tablero)

				# Verificamos que la pieza sea un rey y sea enemigo (turno propio)
				elif(tablero[i][j].__dict__['team'] == jugador.__dict__['equipo'] and tablero[i][j].__dict__['tipo'] == 'Rey'):
					# Ejecutamos los métodos que evalúan si es rey
					pass
				else:
					pass

def ubicacionesDisponiblesRey(rey, tablero):

	posX = rey.posicionX
	posY = rey.posicionY

	multiplicadorY = -1 if rey.__dict__['team'] == 'negro' else 1


	movimientos = [
		[1,1],
		[-1,1],
		[-1,-1],
		[1,-1],
		[1,0],
		[-1,0],
		[0,1],
		[0,-1]
	]


	for i in movimientos:

		x = posX+i[0] if posX+i[0]<= 8 and posX+i[0] >= 0 else None
		y = posY+multiplicadorY*i[1] if posY+multiplicadorY*i[1]<= 8 and posY+multiplicadorY*i[1] >= 0 else None

		if(x != None and y != None):
			if(tablero[x][y] == "  " or tablero[x][y].__dict__['team'] != rey.__dict__['team']):
				# verificamos si esas ubicaciones estan atacadas
				pass



def moverPiezas(tablero, jugador):

	def mueveOro(poxX, posY, tablero, jugador): 
		X = posX + multiplicadorY * 1
		Y = posY 
		vacio = False if tablero[X][Y] == "  " else True
		colorPiezaEnemiga = tablero[X][Y].__dict__['team'] if tablero[X][Y] != "  " else None
		# x, y, pieza, equipo, colorPiezaEnemiga, piezaMovida
		validacion = Peon.movimiento(0, multiplicadorY*1,vacio,str(jugador.equipo),colorPiezaEnemiga, pieza)
		print(validacion)

	for i in range(0,9):
		for j in range(0,9):
			# Movemos las piezas
			if(tablero[i][j] != "  "):
				pieza = tablero[i][j] if tablero[i][j].__dict__['team'] == jugador.__dict__['equipo'] else None
				if(pieza != None):
					posX = pieza.posicionX
					posY = pieza.posicionY
					multiplicadorY = -1 if pieza.__dict__['team'] == 'negro' else 1
					if(pieza.tipo == 'Peón'):
						if(pieza.coronado != True):
							X = posX + multiplicadorY * 1
							Y = posY 
							vacio = False if tablero[X][Y] == "  " else True
							colorPiezaEnemiga = tablero[X][Y].__dict__['team'] if tablero[X][Y] != "  " else None
							# x, y, pieza, equipo, colorPiezaEnemiga, piezaMovida
							validacion = Peon.movimiento(0, multiplicadorY*1,vacio,str(jugador.equipo),colorPiezaEnemiga, pieza)
							print(validacion)

	# Método que moverá todas las piezas enemigas del tablero para ver 


	