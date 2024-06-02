import numpy as np
import matplotlib.pyplot as plt
import random


def busqueda_secuencial_comps(lista, x):
    '''Si x está en la lista devuelve el índice de su primera aparición, 
    de lo contrario devuelve -1. Además devuelve la cantidad de comparaciones
    que hace la función.
    '''
    comps = 0  # inicializo en cero la cantidad de comparaciones
    pos = -1
    for i, z in enumerate(lista):
        comps += 1  # sumo la comparación que estoy por hacer
        if z == x:
            pos = i
            break
    return pos, comps


def busqueda_binaria_comps(lista, x, verbose=False):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
    Además devuelve la cantidad de comparaciones
    que hace la función
    '''
    if verbose:
        print('[DEBUG] izq |der |medio')
    pos = -1  # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    comps = 0
    while izq <= der:
        comps += 1
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1  # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1  # descarto mitad izquierda
    return pos, comps


def generar_lista(cant_elementos, max):
    lista = random.sample(range(max), k=cant_elementos)
    lista.sort()
    return lista


def generar_elemento(max):
    return random.randint(0, max-1)


def experimento_secuencial_promedio(lista, m, k):
    comps_tot = 0
    for i in range(k):
        x = generar_elemento(m)
        comps_tot += busqueda_secuencial_comps(lista, x)[1]

    comps_prom = comps_tot / k
    return comps_prom


def experimento_binario_promedio(lista, m, k):
    comps_tot = 0
    for i in range(k):
        x = generar_elemento(m)
        comps_tot += busqueda_binaria_comps(lista, x)[1]

    comps_prom = comps_tot / k
    return comps_prom


def plot_experimento_secuencial_promedio():
    max = 10000
    veces = 1000

    # estos son los largos de listas que voy a usar
    largos = np.arange(256) + 1
    # aca guardo el promedio de comparaciones sobre una lista de largo i, para i entre 1 y 256.
    comps_promedio = np.zeros(256)

    for i, n in enumerate(largos):
        lista = generar_lista(n, max)  # genero lista de largo n
        comps_promedio[i] = experimento_secuencial_promedio(lista, max, veces)

    # ahora grafico largos de listas contra operaciones promedio de búsqueda.
    plt.plot(largos, comps_promedio, label='Búsqueda Secuencial')
    plt.xlabel("Largo de la lista")
    plt.ylabel("Cantidad de comparaciones")
    plt.title("Complejidad de la Búsqueda")
    plt.legend()
    plt.show()


def plot_experimento_binario_promedio():
    max = 10000
    veces = 1000

    # estos son los largos de listas que voy a usar
    largos = np.arange(256) + 1
    # aca guardo el promedio de comparaciones sobre una lista de largo i, para i entre 1 y 256.
    comps_promedio = np.zeros(256)

    for i, n in enumerate(largos):
        lista = generar_lista(n, max)  # genero lista de largo n
        comps_promedio[i] = experimento_binario_promedio(lista, max, veces)

    # ahora grafico largos de listas contra operaciones promedio de búsqueda.
    plt.plot(largos, comps_promedio, label='Búsqueda Secuencial')
    plt.xlabel("Largo de la lista")
    plt.ylabel("Cantidad de comparaciones")
    plt.title("Complejidad de la Búsqueda")
    plt.legend()
    plt.show()


def graficar_bbin_vs_bseq(max, veces):
    # estos son los largos de listas que voy a usar
    largos = np.arange(256) + 1
    # aca guardo el promedio de comparaciones sobre una lista de largo i, para i entre 1 y 256.
    comps_promedio_secuencial = np.zeros(256)
    comps_promedio_binaria = np.zeros(256)

    for i, n in enumerate(largos):
        lista = generar_lista(n, max)  # genero lista de largo n
        comps_promedio_secuencial[i] = experimento_secuencial_promedio(lista, max, veces)
        comps_promedio_binaria[i] = experimento_binario_promedio(lista, max, veces)

    # Graph both comps_promedio_secuencial and comps_promedio_binaria in the same figure
    plt.plot(largos, comps_promedio_secuencial, label='Búsqueda Secuencial')
    plt.plot(largos, comps_promedio_binaria, label='Búsqueda Binaria')
    plt.xlabel("Largo de la lista")
    plt.ylabel("Cantidad de comparaciones")
    plt.title("Complejidad de la Búsqueda")
    plt.legend()
    plt.xlim(0, 256)
    plt.ylim(0, 40)
    plt.show()


if __name__ == '__main__':
    # plot_experimento_secuencial_promedio()
    # plot_experimento_binario_promedio()
    max = 10000
    veces = 1000
    graficar_bbin_vs_bseq(max, veces)
