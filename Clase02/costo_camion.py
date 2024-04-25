import csv

file_path = '../Data/missing.csv'

costo_total = 0

with open(file_path) as file:
	rows = csv.reader(file)
	next(rows)
	for row in rows:
		try:
			cant_cajones = row[1]
			precio_cajon = row[2]
			costo_total += int(cant_cajones) * float(precio_cajon)
		except ValueError:
			nombre_producto = row[0]
			print(f"Warning: DATOS FALTANTES PARA {nombre_producto.upper()}!")
	
print(f'Costo total: {costo_total}')
