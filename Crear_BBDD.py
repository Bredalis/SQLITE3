
# Programa que crea BBDD

class crearBBDD:

	def __init__(self, bbdd):

		self.bbdd = sqlite.connect(bbdd)
		self.cursor = self.bbdd.cursor()

	def crear_tabla(self, tabla, columna_1, columna_2, columna_3):

		self.cursor.execute(f'CREATE TABLE IF NOT EXISTS {tabla} ("ID" INTEGER PRIMARY KEY, "{columna_1}" TEXT, "{columna_2}" TEXT, "{columna_3}" INTEGER)')

		self.bbdd.commit()
		self.bbdd.close()

if __name__ == '__main__':

	import sqlite3 as sqlite

	crear_bbdd = crearBBDD('BBDD.db')
	crear_bbdd.crear_tabla('Informe', 'Nombre', 'Apellido', 'Edad')