"""Clase de Cuadro del tablero"""

def Cuadro():

	pieza = None
	# Referenciamos la pieza que ocupa el lugar
	posicionX = None
	# Posición X del cuadro
	posicionY = None
	# Posición Y del cuadro
	color = None
	# Color del jugador que ocupa ese cuadro
	ocupada = False
	# Si esta ocupada

	def __init__(self, posicionX, posicionY, pieza, color, ocupada):

		self.pieza = pieza
		self.posicionX = posicionX
		self.posicionY = posicionY
		self.color = color
		self.ocupada = ocupada

	@classmethod
	def inicializarCuadro(self):

		self.pieza = None
		self.ocupada = False
		self.color = None