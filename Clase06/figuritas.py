import random
import numpy as np
import matplotlib.pyplot as plt


def crear_album(figus_total):
    return np.zeros(figus_total, dtype=int)


def album_incompleto(album):
    return not np.all(album)


def comprar_figu(figus_total):
    return random.randint(0, figus_total - 1)


def pegar_figu(album, figu):
    album[figu] += 1
    return album


def cuantas_figus(figus_total):
    cant_figus = 0
    album = crear_album(figus_total)
    while album_incompleto(album):
        cant_figus += 1
        figu = comprar_figu(figus_total)
        album = pegar_figu(album, figu)
        # print(figu)
        # print(album)

    return cant_figus


def experimento_figus(n_repeticiones, figus_total):
    resultados = []
    for i in range(n_repeticiones):
        cant_figus = cuantas_figus(figus_total)
        resultados.append(cant_figus)

    return resultados


def comprar_paquete(figus_total, figus_paquete):
    return [comprar_figu(figus_total) for i in range(figus_paquete)]


def pegar_paquete(album, paquete):
    for figu in paquete:
        album = pegar_figu(album, figu)
    return album


def cuantos_paquetes(figus_total, figus_paquete):
    cant_paquetes = 0
    album = crear_album(figus_total)
    while album_incompleto(album):
        cant_paquetes += 1
        paquete = comprar_paquete(figus_total, figus_paquete)
        album = pegar_paquete(album, paquete)
        # print(figu)
        # print(album)

    return cant_paquetes


def experimento_paquetes(n_repeticiones, figus_total, figus_paquete):
    resultados = []
    for i in range(n_repeticiones):
        cant_paquetes = cuantos_paquetes(figus_total, figus_paquete)
        resultados.append(cant_paquetes)

    return resultados


def calcular_historia_figus_pegadas(figus_total, figus_paquete):
    album = crear_album(figus_total)
    historia_figus_pegadas = [0]
    while album_incompleto(album):
        paquete = comprar_paquete(figus_total, figus_paquete)
        while paquete:
            album[paquete.pop()] = 1
        figus_pegadas = (album > 0).sum()
        historia_figus_pegadas.append(figus_pegadas)
    return historia_figus_pegadas


def graficar_llenado_album(figus_total, figus_paquete):
    plt.plot(calcular_historia_figus_pegadas(figus_total, figus_paquete))
    plt.xlabel("Cantidad de paquetes comprados.")
    plt.ylabel("Cantidad de figuritas pegadas.")
    plt.title("La curva de llenado se desacelera al final")
    plt.show()


def calcular_probabilidad(resultados, limite_paquetes):
    probabilidad = (np.array(resultados_paquetes) <= limite_paquetes).sum() / len(resultados)
    return probabilidad


def histograma_paquetes(resultados):
    plt.hist(resultados, bins=10)
    plt.title("Paquetes comprados por repeticion")
    plt.show()


if __name__ == '__main__':
    figus_total = 670
    n_repeticiones = 1000
    # resultados_figus = experimento_figus(n_repeticiones, figus_total)
    # print(f"Promedio de figus: {np.mean(resultados_figus)}")

    figus_paquete = 5
    resultados_paquetes = experimento_paquetes(n_repeticiones, figus_total, figus_paquete)
    print(f"Promedio de paquetes: {np.mean(resultados_paquetes)}")

    # graficar_llenado_album(figus_total, figus_paquete)

    # probabilidad_menor_850 = calcular_probabilidad(resultados_paquetes, limite_paquetes=850)
    # print(f"La probabilidad de completar el álbum con 850 paquetes o menos es: {probabilidad_menor_850}")

    histograma_paquetes(resultados_paquetes)
