from piezas.pieza import *

# HERENCIA PIEZA
"""ALFIL"""
class Alfil(Pieza):

	corona = True
	coronado = False
	descriptor = ""

	def __init__(self, team, enemy, posicionX, posicionY):

		Pieza.__init__(self, team, enemy, self.corona)
		self.posicionX = posicionX
		self.posicionY = posicionY
		self.descriptorBlanco = "av"
		self.descriptorNegro = "a^"
		self.tipo = 'Alfil'
		if(self.team == 'blanco'):
			self.descriptor = self.descriptorBlanco
		elif(self.team == 'negro'):
			self.descriptor = self.descriptorNegro

	def __str__(self):
		return self.descriptor

	@staticmethod
	def movimiento(x, y, pieza, equipo, colorPiezaEnemiga, piezaMovida):

		movimientoValido = False

		if(( x > -9 and x < 9) and ( y > -9 and y < 9) and x == y ):
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