from piezas.pieza import *

# HERENCIA PIEZA
"""REY"""
class Rey(Pieza):

	corona = False
	descriptor = ""

	def __init__(self, team, enemy, posicionX, posicionY):

		Pieza.__init__(self, team, enemy, self.corona)
		self.posicionX = posicionX
		self.posicionY = posicionY
		self.descriptorBlanco = "Rv"
		self.descriptorNegro = "R^"
		self.tipo = 'Rey'
		if(self.team == 'blanco'):
			self.descriptor = self.descriptorBlanco
		elif(self.team == 'negro'):
			self.descriptor = self.descriptorNegro

	def __str__(self):
		return self.descriptor

	def isCheck(self, tablero):

		# Verificamos que este atacado en la posición actual

		# Verificamos los movimientos posibles del rey
		# def movimientoLibre(tablero):

		# 	movimientos = {[1,1],[1,-1],[-1,1],[-1,-1],[0,1],[0,-1],[1,0],[-1,0]}

		# 	for x in movimientos:
				
		# 		# Verificamos que el tablero este vacío o tenga una pieza enemiga en el casillero con el posible movimiento
		# 		if( (tablero[self.posicionX + x[0]][self.posicionY + x[1]] == "  " or tablero[self.posicionX + x[0]][self.posicionY + x[1]].__dict__['team'] != self.team ) and self.team == 'blanco'):
		# 			return True
		# 		elif( (tablero[self.posicionX + x[0]][self.posicionY + self.multiplicador * x[1]] == "  " or tablero[self.posicionX + x[0]][self.posicionY + self.multiplicador * x[1]].__dict__['team'] != self.team ) and self.team == 'negro'):
		# 			return True
		# 		else:
		# 			return False

		# print(movimientoLibre(tablero))


		return True

	def isCheckMate(self, tablero):
		return False


	@staticmethod
	def movimiento(x, y, pieza, equipo, colorPiezaEnemiga, piezaMovida):

		movimientoValido = False

		if(x == 1 and y == 1 ):
			movimientoValido = True
		elif( x == -1 and y == 1):
			movimientoValido = True
		if(x == -1 and y == -1 ):
			movimientoValido = True
		elif( x == 1 and y == -1):
			movimientoValido = True
		elif(x == 1 and y == 0):
			movimientoValido = True
		elif(x == -1 and y == 0):
			movimientoValido = True
		elif(y == -1 and x == 0):
			movimientoValido = True
		elif(y == 1 and x == 0):
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
