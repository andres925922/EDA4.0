from piezas.pieza import *
"""TORRE"""
class Torre(Pieza):

	corona = True
	coronado = False
	descriptor = ""

	def __init__(self, team, enemy, posicionX, posicionY):

		Pieza.__init__(self, team, enemy, self.corona)
		self.posicionX = posicionX
		self.posicionY = posicionY
		self.descriptorBlanco = "tv"
		self.descriptorNegro = "t^"
		self.tipo = 'Torre'
		if(self.team == 'blanco'):
			self.descriptor = self.descriptorBlanco
		elif(self.team == 'negro'):
			self.descriptor = self.descriptorNegro

	def __str__(self):
		return self.descriptor

	@staticmethod
	def movimiento(x, y, pieza, equipo, colorPiezaEnemiga, piezaMovida):

		movimientoValido = False

		if(( x >= 0 and x < 9 ) and y == 0 ):
			movimientoValido = True
		elif(( y >= 0 and y < 9 ) and x == 0 ):
			movimientoValido = True
		elif((x == -1 or x == 1) and (y == 1 or y == -1) and piezaMovida.__dict__['coronado'] == True):
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

# print('TORRE')
# print('====================================')
# torre = Torre('negro', 'blanco', 2, 7)
# print(torre)

# print(torre.movimiento(0,1)) # Movimiento válido
# print(torre.movimiento(0,3)) # Movimiento válido
# print(torre.movimiento(0,9)) # Movimiento inválido
# print(torre.movimiento(1,0)) # Movimiento válido
# print(torre.movimiento(1,-1)) # Movimiento inválido
# print(torre.movimiento(-1,-1)) # Movimiento inválido