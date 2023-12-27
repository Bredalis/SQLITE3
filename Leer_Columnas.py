
# Programa que muestra los 
# datos de cada columna

class columnas:

	def __init__(self, bbdd, tabla):

		self.bbdd = sqlite.connect(bbdd)
		self.cursor = self.bbdd.cursor()
		self.instruccion = f'SELECT * FROM {tabla}'

	def leer_columnas(self):

		self.cursor.execute(self.instruccion)
		self.datos = self.cursor.fetchall()

		self.bbdd.commit()
		self.bbdd.close()

		return self.datos

if __name__ == '__main__':

	import sqlite3 as sqlite

	columnas = columnas('BBDD.db', 'Informe')
	print(columnas.leer_columnas())