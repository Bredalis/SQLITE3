
# Programa que inserta 
# nuevos datos a las 
# columnas de la tabla

class insertar:

	def __init__(self, bbdd, tabla, ID, columna_1, columna_2, columna_3):

		self.bbdd = sqlite.connect(bbdd)
		self.cursor = self.bbdd.cursor()
		self.instruccion = f'INSERT INTO {tabla} VALUES("{ID}", "{columna_1}", "{columna_2}", {columna_3})'

	def ejecucion(self):

		self.cursor.execute(self.instruccion)

		self.bbdd.commit()
		self.bbdd.close()

if __name__ == '__main__':

	import sqlite3 as sqlite

	insertar = insertar('BBDD.db', 'Informe', '4', 'Lucia', 'Mendoza', 15)
	insertar.ejecucion()