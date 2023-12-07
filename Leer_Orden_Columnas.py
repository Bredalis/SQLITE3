
"""
Programa que muestra 
los datos de las columnas 
en orden
"""

class Orden_Columnas:

	def __init__(self, bbdd, tabla, campo):

		self.bbdd = sqlite.connect(bbdd)
		self.cursor = self.bbdd.cursor()
		self.instruccion = f"SELECT * FROM {tabla} ORDER BY {campo}"

	def Leer_Orden(self):
		
		self.cursor.execute(self.instruccion)
		self.datos = self.cursor.fetchall()

		self.bbdd.commit()
		self.bbdd.close()

		return self.datos

if __name__ == "__main__":

	import sqlite3 as sqlite

	orden_columnas = Orden_Columnas("BBDD.db", "Informe", "Nombre")
	print(orden_columnas.Leer_Orden())