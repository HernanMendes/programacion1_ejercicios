import csv
import sys

def costo_camion(nombre_archivo):
	costo_total = 0

	with open(nombre_archivo) as file:
		rows = csv.reader(file)
		headers = next(rows)
		for i, row in enumerate(rows):
			record = dict(zip(headers, row))
			try:
				cant_cajones = int(record['cajones'])
				precio_cajon = float(record['precio'])
				costo_total += cant_cajones * precio_cajon
			except ValueError:
				print(f"Fila {i}: No pude interpretar: {row}")
	return costo_total
	
