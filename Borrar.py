
"""
Programa que 
borra valores 
de la tabla
"""

class Borrar:

	def __init__(self, bbdd, tabla, columna, valor):

		self.bbdd = sqlite.connect(bbdd)
		self.cursor = self.bbdd.cursor()
		self.instruccion = f"DELETE FROM {tabla} WHERE {columna} = '{valor}'"

	def Ejecucion(self):	

		self.cursor.execute(self.instruccion)

		self.bbdd.commit()
		self.bbdd.close()

if __name__ == "__main__":

	import sqlite3 as sqlite

	borrar = Borrar("BBDD.db", "Informe", "Nombre", "Jonathan")
	borrar.Ejecucion()