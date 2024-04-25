from collections import Counter
import csv


# Ejercicio 4.13: Lectura de los árboles de un parque
def leer_parque(nombre_archivo, parque):
	arboles = []
	with open(nombre_archivo) as file:
		rows = csv.reader(file)
		headers = next(rows)
		for i, row in enumerate(rows):
			record = dict(zip(headers, row))
			if record['espacio_ve'] == parque:
				arboles.append(record)
	return arboles


# Ejercicio 4.14: Determinar las especies en un parque
def especies(lista_arboles):
	especies = []
	for arbol in lista_arboles:
		especies.append(arbol['nombre_com'])
	
	return set(especies)


# Ejercicio 4.15: Contar ejemplares por especie
def contar_ejemplares(lista_arboles):
	ejemplares = Counter()
	for arbol in lista_arboles:
		ejemplares[arbol['nombre_com']] += 1
	return ejemplares


def especies_frecuentes(parques):
	for parque in parques:
		arboles = leer_parque('../Data/arbolado-en-espacios-verdes.csv', parque)
		contador_ejemplares = contar_ejemplares(arboles)
		print(f"Especies mas frecuentes en {parque}: {contador_ejemplares.most_common(5)}")
		

# Ejercicio 4.16: Alturas de una especie en una lista
def obtener_alturas(lista_arboles, especie):
	alturas = []
	for arbol in lista_arboles:
		if arbol['nombre_com'] == especie:
			alturas.append(float(arbol['altura_tot']))
	return alturas

def calcular_max_prom(alturas):
	print(f"Maximo: {max(alturas)}. Prom: {sum(alturas)/len(alturas)}")
	

# Ejercicio 4.17: Inclinaciones por especie de una lista
def obtener_inclinaciones(lista_arboles, especie):
	inclinaciones = []
	for arbol in lista_arboles:
		if arbol['nombre_com'] == especie:
			inclinaciones.append(int(arbol['inclinacio']))
	return inclinaciones
	
# Ejercicio 4.18: Especie con el ejemplar más inclinado
def especimen_mas_inclinado(lista_arboles):
	especies_unicas = especies(lista_arboles)
	inclinacion_maxima = 0
	especie_inclinacion_maxima = ''
	for especie in especies_unicas:
		inclinaciones = obtener_inclinaciones(lista_arboles, especie)
		
		if max(inclinaciones) > inclinacion_maxima:
			inclinacion_maxima = max(inclinaciones)
			especie_inclinacion_maxima = especie
			
	return especie_inclinacion_maxima, inclinacion_maxima
		
	
# Ejercicio 4.19: Especie más inclinada en promedio
def especie_promedio_mas_inclinada(lista_arboles):
	especies_unicas = especies(lista_arboles)
	inclinacion_maxima = 0
	especie_inclinacion_maxima = ''
	for especie in especies_unicas:
		inclinaciones = obtener_inclinaciones(lista_arboles, especie)
		inclinacion_promedio = sum(inclinaciones)/len(inclinaciones)
		if inclinacion_promedio > inclinacion_maxima:
			inclinacion_maxima = max(inclinaciones)
			especie_inclinacion_maxima = especie
			
	return especie_inclinacion_maxima, inclinacion_maxima
	
# Preguntas extras
def leer_ciudad(nombre_archivo):
	arboles = []
	with open(nombre_archivo) as file:
		rows = csv.reader(file)
		headers = next(rows)
		for i, row in enumerate(rows):
			record = dict(zip(headers, row))
			arboles.append(record)
	return arboles

def ejemplar_mas_inclinado_ciudad():
	nombre_archivo = '../Data/arbolado-en-espacios-verdes.csv'
	arboles = leer_ciudad(nombre_archivo)
	especimen = especimen_mas_inclinado(arboles)

	for arbol in arboles:
		if arbol['inclinacio'] == str(especimen[1]):
			print(f"Especie: {especimen[0]}")
			print(f"Inclinacion: {especimen[1]}°")
			print(f"Latitud: {arbol['lat']}")
			print(f"Longitud: {arbol['long']}")
			print()
			

def ejemplar_mas_alto_ciudad():
	nombre_archivo = '../Data/arbolado-en-espacios-verdes.csv'
	arboles = leer_ciudad(nombre_archivo)
	
	alturas = []
	for arbol in arboles:
		alturas.append(int((arbol['altura_tot'])))
	altura_maxima = max(alturas)

	for arbol in arboles:
		if arbol['altura_tot'] == str(altura_maxima):
			print(f"Especie: {arbol['nombre_com']}")
			print(f"Altura: {arbol['altura_tot']}m")
			print(f"Latitud: {arbol['lat']}")
			print(f"Longitud: {arbol['long']}")
			print()
			
	
	
