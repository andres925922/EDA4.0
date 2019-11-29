from piezas.pieza import *


"""PEON"""
class Peon(Pieza):

	corona = True
	coronado = False
	descriptor = ""

	def __init__(self, team, enemy, posicionX, posicionY):

		Pieza.__init__(self, team, enemy, self.corona)
		self.posicionX = posicionX
		self.posicionY = posicionY
		self.coronado = False
		self.descriptorBlanco = "pv"
		self.descriptorNegro = "p^"
		self.tipo = 'Peón'

		if(self.team == 'blanco'):
			self.descriptor = self.descriptorBlanco
		elif(self.team == 'negro'):
			self.descriptor = self.descriptorNegro
			
		# if(self.coronado == True):
			

	def __str__(self):
		return self.descriptor


	@staticmethod
	@peonDecorado
	# Habilita los movimientos del general de Oro
	def movimiento(x, y, pieza, equipo, colorPiezaEnemiga, piezaMovida):

		movimientoValido = False

		# Mueve hacia adelante y diagonales hacia adelante en una posición
		# Mueve hacia atrás solo en dirección vertical 

		if(x == 0 and y == 1):

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

# print('PEON')
# print('====================================')
# peon = Peon('negro', 'blanco', 1, 6)
# print(peon)

# print(peon.movimiento(0,1)) # Movimiento válido
# print(peon.movimiento(0,3)) # Movimiento inválido
# print(peon.movimiento(0,9)) # Movimiento inválido
# print(peon.movimiento(1,0)) # Movimiento inválido
# print(peon.movimiento(1,-1)) # Movimiento inválido
# print(peon.movimiento(-1,-1)) # Movimiento inválido
