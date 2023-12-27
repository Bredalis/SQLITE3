
# Programa que muestra los
# datos de las columnas en orden

class orden_columnas:

	def __init__(self, bbdd, tabla, campo):

		self.bbdd = sqlite.connect(bbdd)
		self.cursor = self.bbdd.cursor()
		self.instruccion = f"SELECT * FROM {tabla} ORDER BY {campo}"

	def leer_orden(self):
		
		self.cursor.execute(self.instruccion)
		self.datos = self.cursor.fetchall()

		self.bbdd.commit()
		self.bbdd.close()

		return self.datos

if __name__ == "__main__":

	import sqlite3 as sqlite

	orden_columnas = orden_columnas("BBDD.db", "Informe", "Nombre")
	print(orden_columnas.leer_orden())