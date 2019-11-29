class Pieza():

	def __init__(self, color):

		self.color = color


tablero = [' ']*9

def main():

	for i in range(0,9):
		tablero[i] = [' ']*9

	for i in range(0,9):
		for j in range(0,9):

			if(j == 1 or j == 7):
				tablero[i][j] = Pieza('red').color
			elif((i == 0 or i == 7) and (j == 0 or j == 8)):
				tablero[i][j] = 'T'
			elif((i == 1 or i == 6) and (j == 0 or j == 8)):
				tablero[i][j] = 'C'
			elif((i == 2 or i == 5) and (j == 0 or j == 8)):
				tablero[i][j] = 'A'


	for i in range(0,9):
		line = ''
		for j in range(0,9):
			line += "{} ".format(tablero[j][i])


		print(line)

		print('\n')

if __name__ == '__main__':
	main() 
