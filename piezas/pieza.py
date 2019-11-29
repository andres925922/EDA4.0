
class Pieza():

	# Clase padre para todas las piezas

	def __init__(self, team, enemy, corona):

		self.team = team
		# color del equipo
		self.corona = corona
		# Pieza que corona
		self.posicionX = None
		self.posicionY = None
		self.posicionXY = None
		# Posición de la pieza

	def cambiarEquipo(self, equipo):
		self.team = equipo
		if(self.team == 'blanco'):
			self.descriptor = self.descriptorBlanco
		elif(self.team == 'negro'):
			self.descriptor = self.descriptorNegro

	@staticmethod
	def comePieza(colorPiezaEnemiga, team):

		# Verificamos si la pieza que vamos a atacar es del mismo equipo o no. Sinó no podrá avanzar
		# Solo debe ejecutarse en caso de que exista una pieza en el lugar

		if(colorPiezaEnemiga != team):
			return True
		else:
			return False
		pass

	# FUNCIÓN QUE VALIDA SI EL MOVIMIENTO ES VÁLIDO Y SI PUEDE COMER LA PIEZA
	# En caso de que haya una pieza frente

	def validaMovimiento(self, movimientoValido, pieza, colorPiezaEnemiga):

		if(pieza == True):
			if(self.comePieza(colorPiezaEnemiga)):
				return True
			else:
				return False

		return True




	# FUNCIÓN PARA CORONAR PIEZAS
	def coronar(self):

		if(self.corona == True):
			if( self.posicionX <= 2 and self.team == 'negro'):
				self.coronado = True
				self.descriptor = self.descriptor.upper()
				# self.descriptor = "+"+self.descriptor
			elif( self.posicionX >= 6 and self.team == 'blanco'):
				self.coronado = True
				self.descriptor = self.descriptor.upper()
				# self.descriptor = "+"+self.descriptor


def peonDecorado(f):
	def movimientoCoronado(x, y, pieza, equipo, colorPiezaEnemiga, piezaMovida):

		if(piezaMovida.__dict__['coronado'] == True):

			movimientoValido = False

			# Mueve hacia adelante, izquiera, derecha y diagonales hacia adelante en una posición
			# Mueve hacia atrás solo en dirección vertical 

			if(x == 1 and y == 1 ):
				movimientoValido = True
			elif( x == -1 and y == 1):
				movimientoValido = True
			elif(x == 1 and y == 0):
				movimientoValido = True
			elif(x == -1 and y == 0):
				movimientoValido = True
			elif(y == -1 and x == 0):
				movimientoValido = True
			elif(y == 1 and x == 0):
				movimientoValido = True
			else:
				movimientoValido = False

			# Validamos que el movimiento sea válido
			if(movimientoValido == True):
				if(pieza == True): 
				# Validamos si existe una pieza ocupando el lugar a donde se moverá
					if(Pieza.comePieza(colorPiezaEnemiga, equipo)):
						return True
					else:
						return False
				else:
					return True
			else:
				return False


		else:
			return f(x, y, pieza, equipo, colorPiezaEnemiga, piezaMovida)


	return movimientoCoronado




