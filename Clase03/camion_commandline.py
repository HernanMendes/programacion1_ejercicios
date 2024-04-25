# camion_commandline.py
import csv
import sys

def costo_camion(nombre_archivo):
    costo_total = 0

    with open(nombre_archivo) as file:
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
    return costo_total


if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = '../Data/camion.csv'

costo = costo_camion(nombre_archivo)
print('Costo total:', costo)
