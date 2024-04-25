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


def hacer_informe(camion,precios):
	informe = []
	for producto in camion:
		nombre = producto['nombre']
		cajones = producto['cajones']
		precio = producto['precio']
		cambio = precios[nombre] - precio
		registro = (nombre, cajones, precio, cambio)
		informe.append(registro)
	return informe 
	

def main():
	camion = leer_camion('../Data/camion.csv')
	precios = leer_precios('../Data/precios.csv')
	informe = hacer_informe(camion, precios)
	
	headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
	print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
	print(f"{('-'*10+' ')*len(headers)}")
	for nombre, cajones, precio, cambio in informe:
		print(f'{nombre:>10s} {cajones:>10d} {"$"+str(precio):>10s} {cambio:>10.2f}')


if __name__ == '__main__':
	main()
	
	

