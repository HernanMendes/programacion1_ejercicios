def buscar_u_elemento(lista, elemento):
    pos = -1
    i = 0
    for item in lista:
        if item == elemento:
            pos = i
        i += 1

    return pos


def buscar_n_elemento(lista, elemento):
    cant = 0
    for item in lista:
        if item == elemento:
            cant += 1

    return cant


def maximo(lista):
    maximo = lista[0]
    for elem in lista:
        if elem > maximo:
            maximo = elem
    return maximo


def minimo(lista):
    minimo = lista[0]
    for elem in lista:
        if elem < minimo:
            minimo = elem
    return minimo
