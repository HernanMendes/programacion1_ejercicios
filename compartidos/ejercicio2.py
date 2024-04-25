import csv
import numpy as np
from collections import Counter
# import sys
import matplotlib.pyplot as plt


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
    peliculas_autor = [
        pelicula
        for pelicula in peliculas
        if pelicula["Director"] == autor
    ]
    
    return peliculas_autor


def presupuesto_total(peliculas):
    total = sum([
        float(pelicula["Budget"].lstrip('$'))
        for pelicula in peliculas
    ])
    
    return total


def ingresos_promedio(peliculas):
    ingresos = [
        float(pelicula["Revenue"].lstrip('$'))
        for pelicula in peliculas
    ]
    promedio = np.mean(ingresos)
    return promedio


def top3_generos(peliculas):
    top = Counter()

    for pelicula in peliculas:
        genero = pelicula["Genre 1"]
        top[genero] += 1
    
    return top.most_common(3)


# print(sys.argv)

# plt.scatter(X, Y)
# plt.show()

ruta = 'Studio Ghibli.csv'
peliculas = leer_dataset(ruta)

peliculas_isao = peliculas_por_autor(peliculas, "Isao Takahata")
peliculas_hayao = peliculas_por_autor(peliculas, "Hayao Miyazaki")

presupuesto_total_isao = presupuesto_total(peliculas_isao)
ingresos_promedio_hayao = ingresos_promedio(peliculas_hayao)

top3 = top3_generos(peliculas)