
"""
Programa que crea BBDD
"""

class Crear_BBDD:

	def __init__(self, bbdd):

		self.bbdd = sqlite.connect(bbdd)
		self.cursor = self.bbdd.cursor()

	def Crear_Tabla(self, tabla, columna_1, columna_2, columna_3):

		self.cursor.execute(f"""CREATE TABLE IF NOT EXISTS {tabla} ("ID" INTEGER PRIMARY KEY, "{columna_1}" TEXT, "{columna_2}" TEXT, "{columna_3}" INTEGER)""")

		self.bbdd.commit()
		self.bbdd.close()

if __name__ == "__main__":

	import sqlite3 as sqlite

	crear_bbdd = Crear_BBDD("BBDD.db")
	crear_bbdd.Crear_Tabla("Informe", "Nombre", "Apellido", "Edad")