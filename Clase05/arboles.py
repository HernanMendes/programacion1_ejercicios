import csv


# Ejercicio 5.15: Lectura de todos los árboles
def leer_arboles(nombre_archivo):
	with open(nombre_archivo) as file:
		rows = csv.reader(file)
		headers = next(rows)
		return [dict(zip(headers,row)) for row in rows]
	

# Ejercicio 5.16: Lista de altos de Jacarandá
def alturas_especie(especie='Jacarandá'):
    arboleda = leer_arboles('../Data/arbolado-en-espacios-verdes.csv')
    return [float(arbol['altura_tot']) for arbol in arboleda if arbol['nombre_com'] == especie]


# Ejercicio 5.17: Lista de altos y diámetros de Jacarandá
def alturas_diam_especie(especie='Jacarandá'):
    arboleda = leer_arboles('../Data/arbolado-en-espacios-verdes.csv')
    return [(float(arbol['altura_tot']),float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com'] == especie]


# Ejercicio 5.18: Diccionario con medidas
def medidas_de_especies(especies,arboleda):
    return {especie: [(float(arbol['altura_tot']),float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com'] == especie] for especie in especies}
    