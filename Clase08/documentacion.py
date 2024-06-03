def valor_absoluto(n):
    """Calcula el valor absoluto de un número.

    pre: n debe ser un número real.
    post: devuelve el valor absoluto de n.
    """
    if n >= 0:
        return n
    else:
        return -n


def suma_pares(l):
    """Suma los números pares de una lista.

    pre: l debe ser una lista de números.
    post: devuelve la suma de los números pares de l.
    """
    res = 0
    for e in l:
        if e % 2 == 0:
            res += e
        else:
            res += 0

    return res


def veces(a, b):
    """Multiplica a por b.

    pre: a y b deben ser números enteros.
    post: devuelve el resultado de multiplicar a por b.
    """
    res = 0
    nb = b
    while nb != 0:
        # print(nb * a + res)
        res += a
        nb -= 1
    return res


def collatz(n):
    """Calcula la conjetura de Collatz para n.

    pre: n debe ser un número entero positivo.
    post: devuelve la cantidad de pasos necesarios para llegar a 1.
    """
    res = 1

    while n != 1:
        if n % 2 == 0:
            n = n//2
        else:
            n = 3 * n + 1
        res += 1

    return res
