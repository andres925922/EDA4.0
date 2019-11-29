
from piezas.pieza import *

"""CABALLO"""
class Caballo(Pieza):

	corona = True
	coronado = False
	descriptor = ""

	def __init__(self, team, enemy, posicionX, posicionY):

		Pieza.__init__(self, team, enemy, self.corona)
		self.posicionX = posicionX
		self.posicionY = posicionY
		self.coronado = False
		self.descriptorBlanco = "cv"
		self.descriptorNegro = "c^"
		self.tipo = 'Caballo'

		if(self.team == 'blanco'):
			self.descriptor = self.descriptorBlanco
		elif(self.team == 'negro'):
			self.descriptor = self.descriptorNegro

	def __str__(self):
		return self.descriptor

	@staticmethod
	@peonDecorado
	def movimiento(x, y, pieza, equipo, colorPiezaEnemiga, piezaMovida):

		movimientoValido = False

		# Mueve hacia adelante y diagonales hacia adelante en una posición
		# Mueve hacia atrás solo en dirección vertical 

		if(x == 1 and y == 2 ):
			movimientoValido = True
		elif( x == -1 and y == 2):
			movimientoValido = True

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


# print('CABALLO')
# print('====================================')
# caballo = Caballo('negro', 'blanco', 1, 8)
# print(caballo)

# print(caballo.movimiento(1,2)) # Movimiento válido
# print(caballo.movimiento(-1,2)) # Movimiento válido
# print(caballo.movimiento(1,0)) # Movimiento inválido
# print(caballo.movimiento(1,-1)) # Movimiento inválido
# print(caballo.movimiento(-1,-1)) # Movimiento inválido
