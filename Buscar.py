
# Pragrama que busca 
# y muestra valores

class buscar:

	def __init__(self, bbdd, tabla, columna, valor):

		self.bbdd = sqlite.connect(bbdd)
		self.cursor = self.bbdd.cursor()
		self.instruccion = f'SELECT * FROM {tabla} WHERE {columna} = "{valor}"'

	def ejecucion(self):

		self.cursor.execute(self.instruccion)
		self.datos = self.cursor.fetchall()

		self.bbdd.commit()
		self.bbdd.close()

		return self.datos

if __name__ == '__main__':

	import sqlite3 as sqlite

	buscar = buscar('BBDD.db', 'Informe', 'Nombre', 'Jonathan')
	print(buscar.ejecucion())