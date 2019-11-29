
from piezas.pieza import *

"""LANCERO"""
class Lancero(Pieza):

	corona = True
	descriptor = ""

	def __init__(self, team, enemy, posicionX, posicionY):

		Pieza.__init__(self, team, enemy, self.corona)
		self.posicionX = posicionX
		self.posicionY = posicionY
		self.coronado = False
		self.descriptorBlanco = "lv"
		self.descriptorNegro = "l^"
		self.tipo = 'Lancero'

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

		if(x == 0 and (y >= 0 and y < 9) ):
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


# print('LANCERO')
# print('====================================')
# lancero = Lancero('negro', 'blanco', 1, 8)
# print(lancero)

# print(lancero.movimiento(0,1)) # Movimiento válido
# print(lancero.movimiento(0,3)) # Movimiento válido
# print(lancero.movimiento(0,9)) # Movimiento inválido
# print(lancero.movimiento(1,0)) # Movimiento inválido
# print(lancero.movimiento(1,-1)) # Movimiento inválido
# print(lancero.movimiento(-1,-1)) # Movimiento inválido
