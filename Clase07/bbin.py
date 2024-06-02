def busqueda_binaria(lista, x, verbose=False):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
    '''
    if verbose:
        print('[DEBUG] izq |der |medio')
    pos = -1  # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1  # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1  # descarto mitad izquierda
    return pos


def donde_insertar(lista, x, verbose=False):
    if verbose:
        print('[DEBUG] izq |der |medio')
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1  # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1  # descarto mitad izquierda
    return izq


def insertar(lista, x):
    if x in lista:
        return lista.index(x)
    else:
        posicion = donde_insertar(lista, x)
        lista.insert(posicion, x)
        return posicion


if __name__ == '__main__':
    lista = [0, 1, 2, 5]
    n_insertar = 3
    print(f'Lista original: {lista}')
    print(f'Número a insertar: {n_insertar}')
    pos = insertar(lista, n_insertar)
    print(f'Posición donde se insertó: {pos}')
    print(f'Lista luego de insertar: {lista}')
