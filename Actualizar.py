
"""
Programa que actualiza 
valores de las columnas 
de la tabla
"""

class Actualizar:

	def __init__(self, bbdd, tabla, columna, valor_1, ubicacion, valor_2):

		self.bbdd = sqlite.connect(bbdd)
		self.cursor = self.bbdd.cursor()
		self.instruccion = f"UPDATE {tabla} SET {columna} = '{valor_1}' WHERE {ubicacion} = '{valor_2}'"

	def Ejecucion(self):

		self.cursor.execute(self.instruccion)

		self.bbdd.commit()
		self.bbdd.close()

if __name__ == "__main__":

	import sqlite3 as sqlite

	actualizar = Actualizar("BBDD.db", "Informe", "Nombre", "Lucas", "ID", "2")
	actualizar.Ejecucion()