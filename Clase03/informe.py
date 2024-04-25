# fragmento de costo_camion.py
import csv


def leer_camion(nombre_archivo):
	'''Computa el precio total del camion (cajones * precio) de un archivo'''
	camion = []

	with open(nombre_archivo, 'rt') as f:
		rows = csv.reader(f)
		headers = next(rows)
		for row in rows:
			lote = {
				'nombre': row[0],
				'cajones': int(row[1]),
				'precio': float(row[2])
			}
			camion.append(lote)
	return camion


def leer_precios(nombre_archivo):
    precios = {}

    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            if len(row) > 0:
                precios[row[0]] = float(row[1])
    return precios


camion = leer_camion('../Data/camion.csv')
precios = leer_precios('../Data/precios.csv')

costo_camion = 0.0
venta = 0.0
for producto in camion:
    costo_camion += producto['cajones'] * producto['precio']
    venta += producto['cajones'] * precios[producto['nombre']]    

print(f'El costo del camion fue de: ${costo_camion:.2f}')
print(f'Lo que se recaudo con la venta fue de: ${venta:.2f}', end='\n\n')

diferencia = venta - costo_camion
if diferencia >= 0:
    print(f'La ganancia fue de: ${diferencia:.2f}')
else:
    print(f'La perdida fue de: ${diferencia:.2f}')
