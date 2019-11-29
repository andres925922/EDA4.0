
class Jugador():

	def __init__(self, equipo, equipoContrario):

		self.equipo = equipo
		self.equipoContrario = equipoContrario
		self.movimiento = 0
		self.tiempo = 0
		self.check = False
		self.PIEZAS_CAPTURADAS = []

		pass

	# Método para introducir pieza capturada en el tablero
	@staticmethod
	def introducirPieza(jugador, tablero):

		# Variable para evaluar si el movimiento es válido
		movimientoValido = False
		# Variable para contar intentos de movimientos erróneos
		contadorMovimientoInvalido = 0

		primerEv = False
		segundaEv = False

		while movimientoValido != True and contadorMovimientoInvalido < 2:

			if(int(len(jugador.PIEZAS_CAPTURADAS)) == 0):
				return False

			indexPieza = int(input('Ingrese el número de la pieza a introducir en el tablero\n'))
			# jugador, tablero, indexPieza
			# Evaluamos que la ubicación en el tablero este desocupada
			xy = input("Ingrese el lugar donde quiere ingresar la pieza (fila, columna separadas por espacio)\n")
			x = int(xy[0])
			y = int(xy[2])

			# Obtenemos la pieza de la lista de piezas capturadas
			newPieza = jugador.__dict__['PIEZAS_CAPTURADAS'][indexPieza]

			if(tablero[x][y] != "  "):
				return False

			# Evaluamos si hay un peon de nuestro equipo en esa columna (solo en caso de que querramos insertar un peón)
			if(newPieza.tipo == 'Peón'):
				isAPeon = False

				for i in range(0,9):
					if(tablero[i][y] != '  '):
						if(tablero[i][y].team == jugador.equipo and tablero[i][y].tipo == 'Peón'):
							isAPeon = True
							continue

				if(isAPeon == True):
					try:
						problema = input('Hay almenos un peon ubicado en esta columna. No puede introducir un peón. Desea elegir otra pieza o cambiar el movimiento (presione 1 o 2 respectivamente)')
					except Exception:
						problema = input('INGRESE UN VALOR VÁLIDO \n')
					if(int(problema) == 1):
						contadorMovimientoInvalido = contadorMovimientoInvalido + 1
						movimientoValido = False
						continue
					elif(int(problema)) == 2:
						return False
				else:
					primerEv = True


				# Peones y lanceros no pueden ser introducidos en la ultima fila
				if((newPieza.tipo == "Peón" and primerEv == True) or newPieza.tipo == "Lancero"):
					if(jugador.equipo == "blanco" and x == 9):
						_problema = input('La pieza seleccionada no puede ser introducida en la ubicación deseada. Desea elegir otra pieza o cambiar el movimiento (presione 1 o 2 respectivamente)')
						if(int(_problema) == 1):
							contadorMovimientoInvalido = contadorMovimientoInvalido + 1
							movimientoValido = False
							continue
						elif(int(_problema)) == 2:
							return False
					elif(jugador.equipo == "negro" and x == 1):
						_problema = input('La pieza seleccionada no puede ser introducida en la ubicación deseada. Desea elegir otra pieza o cambiar el movimiento (presione 1 o 2 respectivamente)')
						if(int(_problema) == 1):
							contadorMovimientoInvalido = contadorMovimientoInvalido + 1
							movimientoValido = False
							continue
						elif(int(_problema)) == 2:
							return False
					else:
						segundaEv = True

				# Los caballos no pueden ingresarse ni en la ultima ni penúltima fila
				if(newPieza.tipo == "Caballo"):
					if(jugador.equipo == "blanco" and x >= 8):
						_problema = input('La pieza seleccionada no puede ser introducida en la ubicación deseada. Desea elegir otra pieza o cambiar el movimiento (presione 1 o 2 respectivamente)')
						if(int(_problema) == 1):
							contadorMovimientoInvalido = contadorMovimientoInvalido + 1
							movimientoValido = False
							continue
						elif(int(_problema)) == 2:
							return False
					elif(jugador.equipo == "negro" and x <= 2):
						_problema = input('La pieza seleccionada no puede ser introducida en la ubicación deseada. Desea elegir otra pieza o cambiar el movimiento (presione 1 o 2 respectivamente)')
						if(int(_problema) == 1):
							contadorMovimientoInvalido = contadorMovimientoInvalido + 1
							movimientoValido = False
							continue
						elif(int(_problema)) == 2:
							return False
					else:
						segundaEv = True
				# Las piezas al ingresar no se coronan, hay que esperar un turno para coronarlas
			if(primerEv == True and segundaEv == True):
				movimientoValido = True

			if(movimientoValido == True):
				jugador.__dict__['PIEZAS_CAPTURADAS'].pop(indexPieza)
				# Cambiamos el equipo de la pieza capturada (al reproducir nuevamente el tablero aparecerá con el símbolo que corresponde)
				newPieza.cambiarEquipo(jugador.__dict__['equipo'])
				# Si la pieza se corona, le ponemos en falso este campo
				if(newPieza.__dict__['corona'] == True):
					newPieza.__dict__['coronado'] = False
				# Retornamos el tablero. Deberemos inicializarlo nuevamente.
				tablero[x][y] = newPieza

				return tablero

