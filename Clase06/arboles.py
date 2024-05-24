import csv
import matplotlib.pyplot as plt


# Ejercicio 5.15: Lectura de todos los árboles
def leer_arboles(nombre_archivo):
    with open(nombre_archivo) as file:
        rows = csv.reader(file)
        headers = next(rows)
        return [dict(zip(headers, row)) for row in rows]


# Ejercicio 5.16: Lista de altos de Jacarandá
def alturas_especie(especie='Jacarandá'):
    arboleda = leer_arboles('../Data/arbolado-en-espacios-verdes.csv')
    return [float(arbol['altura_tot']) for arbol in arboleda if arbol['nombre_com'] == especie]


# Ejercicio 5.17: Lista de altos y diámetros de Jacarandá
def alturas_diam_especie(especie='Jacarandá'):
    arboleda = leer_arboles('../Data/arbolado-en-espacios-verdes.csv')
    return [(float(arbol['altura_tot']), float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com'] == especie]


# Ejercicio 5.18: Diccionario con medidas
def medidas_de_especies(especies, arboleda):
    return {especie: [(float(arbol['altura_tot']), float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com'] == especie] for especie in especies}


# Ejercicio 6.10: Ejercicio 6.10: Histograma de altos de Jacarandás
def histograma_altura():
    nombre_archivo = '../Data/arbolado-en-espacios-verdes.csv'
    nombre_especie = 'Jacarandá'
    arbolada = leer_arboles(nombre_archivo)
    alturas = [arbol['altura_tot'] for arbol in arbolada if arbol['nombre_com'] == nombre_especie]
    plt.hist(alturas, bins=25)
    plt.show()


# Ejercicio 6.11: Scatterplot (diámetro vs alto) de Jacarandás
def scatter_hd(lista_de_pares, especie='Jacarandá'):
    h = [par[0] for par in lista_de_pares]
    d = [par[1] for par in lista_de_pares]

    # h, d = zip(*lista_de_pares)

    plt.scatter(d, h, c='crimson', alpha=0.1)
    plt.xlabel("diametro (cm)")
    plt.ylabel("alto (m)")
    plt.title(f"Relación diámetro-alto para {especie}")
    plt.show()


def scatter_together():
    nombre_archivo = '../Data/arbolado-en-espacios-verdes.csv'
    arboleda = leer_arboles(nombre_archivo)
    especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
    medidas_especies = medidas_de_especies(especies, arboleda)

    fig, ax = plt.subplots()
    ax.set_title("Relación diámetro-alto")

    i = 0
    colors = ['lightcoral', 'lightgreen', 'paleturquoise']

    for especie, medidas in medidas_especies.items():
        h = [par[0] for par in medidas]
        d = [par[1] for par in medidas]

        # h, d = zip(*lista_de_pares)

        ax.scatter(d, h, c=colors[i], alpha=0.1, label=especie)
        ax.set_xlabel("diametro (cm)")
        ax.set_ylabel("alto (m)")
        i += 1

    ax.legend()
    plt.xlim(0, 100)
    plt.ylim(0, 30)
    plt.show()


if __name__ == '__main__':
    histograma_altura()

    pares_hd = alturas_diam_especie()
    scatter_hd(pares_hd)

    scatter_together()
