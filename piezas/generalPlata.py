from piezas.pieza import *

"""GENERAL DE PLATA"""
class generalPlata(Pieza):

	corona = True
	descriptor = ""

	def __init__(self, team, enemy, posicionX, posicionY):

		Pieza.__init__(self, team, enemy, self.corona)
		self.posicionX = posicionX
		self.posicionY = posicionY
		self.coronado = False
		self.descriptorBlanco = "sv"
		self.descriptorNegro = "s^"
		self.tipo = 'GeneralPlata'

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

		if(x == 1 and y == 1 ):
			movimientoValido = True
		elif( x == -1 and y == 1):
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


# print('GENERAL DE PLATA')
# print('====================================')
# general_plata = generalPlata('negro', 'blanco', 3, 8)
# print(general_plata)

# print(general_plata.movimiento(1,1)) # Movimiento válido
# print(general_plata.movimiento(-1,1)) # Movimientoválido
# print(general_plata.movimiento(1,0)) # Movimiento inválido
# print(general_plata.movimiento(1,-1)) # Movimiento inválido
# print(general_plata.movimiento(-1,-1)) # Movimiento inválido

# print('=============================================')
# print('movemos hacia adelante y comemos una pieza blanca')
# print(general_plata.movimiento(1,1,True, 'blanco'))

# print('=============================================')
# print('movemos hacia adelante y tenemos una pieza negra')
# print(general_plata.movimiento(1,1,True, 'negro'))
