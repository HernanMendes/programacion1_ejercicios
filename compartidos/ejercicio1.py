import csv
from collections import Counter


def leer_dataset(direccion):
    peliculas = []

    with open(file=direccion, mode="rt") as f:
        filas = csv.reader(f)
        cabecera = next(filas)
        for fila in filas:
            pelicula = dict(zip(cabecera, fila))
            peliculas.append(pelicula)
    
    return peliculas


def peliculas_por_autor(peliculas, autor):
    peliculas_autor = []

    for pelicula in peliculas:
        if pelicula["Director"] == autor:
            peliculas_autor.append(pelicula)
    
    return peliculas_autor


def presupuesto_total(peliculas):
    total = 0.0

    for pelicula in peliculas:
        presupuesto = str(pelicula["Budget"]).lstrip('$')
        total += float(presupuesto)
    
    return total


def ingresos_promedio(peliculas):
    promedio = 0.0
    suma_ingresos = 0.0

    for pelicula in peliculas:
        ingreso = str(pelicula["Revenue"]).lstrip('$')
        suma_ingresos += float(ingreso)
    
    promedio = suma_ingresos / len(peliculas)
    return promedio


def top3_generos(peliculas):
    top = Counter()

    for pelicula in peliculas:
        genero = pelicula["Genre 1"]
        top[genero] += 1
    
    return top.most_common(3)


direccion = 'Studio Ghibli.csv'
peliculas = leer_dataset(direccion)

peliculas_isao = peliculas_por_autor(peliculas, "Isao Takahata")
peliculas_hayao = peliculas_por_autor(peliculas, "Hayao Miyazaki")

presupuesto_total_isao = presupuesto_total(peliculas_isao)
print(presupuesto_total_isao)
ingresos_promedio_hayao = ingresos_promedio(peliculas_hayao)
print(ingresos_promedio_hayao)

top3 = top3_generos(peliculas)