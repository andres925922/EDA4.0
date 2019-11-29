from piezas.pieza import *

"""GENERAL DE ORO"""
class generalOro(Pieza):

	corona = False
	descriptor = ""

	def __init__(self, team, enemy, posicionX, posicionY):

		Pieza.__init__(self, team, enemy, self.corona)
		self.posicionX = posicionX
		self.posicionY = posicionY
		self.descriptorBlanco = "Ov"
		self.descriptorNegro = "O^"
		self.tipo = 'GeneralOro'

		if(self.team == 'blanco'):
			self.descriptor = self.descriptorBlanco
		else:
			self.descriptor = self.descriptorNegro

	def __str__(self):
		return self.descriptor

	@staticmethod
	def movimiento(x, y, pieza, equipo, colorPiezaEnemiga, piezaMovida):

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

# print('GENERAL DE ORO')
# print('====================================')
# general_oro = generalOro('negro', 'blanco', 3, 8)
# print(general_oro)

# print(general_oro.movimiento(1,1))
# print(general_oro.movimiento(-1,1))
# print(general_oro.movimiento(1,-1))
# print(general_oro.movimiento(-1,-1))

# print('=============================================')
# print('movemos hacia adelante y comemos una pieza blanca')
# print(general_oro.movimiento(1,1,True, 'blanco'))

# print('=============================================')
# print('movemos hacia adelante y tenemos una pieza negra')
# print(general_oro.movimiento(1,1,True, 'negro'))