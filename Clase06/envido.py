import random
from collections import Counter


def repartir_cartas():
    valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
    palos = ['oro', 'copa', 'espada', 'basto']
    naipes = [(valor, palo) for valor in valores for palo in palos]
    cartas = random.sample(naipes, k=3)
    # print(cartas)
    return cartas


def hay_envido(cartas):
    contador_palos = Counter([carta[1] for carta in cartas])
    if contador_palos.most_common(1)[0][1] >= 2:
        return True
    return False


def calcular_envido(cartas):
    contador_palos = Counter([carta[1] for carta in cartas])
    palo, repeticiones = contador_palos.most_common(1)[0]
    if repeticiones >= 2:
        numeros_envido = []
        for carta in cartas:
            if carta[1] == palo:
                if carta[0] in [10, 11, 12]:
                    numeros_envido.append(0)
                else:
                    numeros_envido.append(carta[0])
        numeros_envido.sort(reverse=True)
        envido = sum(numeros_envido[:2]) + 20
        # print(envido)
        return envido
    else:
        numeros_envido = []
        for carta in cartas:
            if carta[0] in [10, 11, 12]:
                numeros_envido.append(0)
            else:
                numeros_envido.append(carta[0])
        numeros_envido.sort(reverse=True)
        envido = sum(numeros_envido[:1])
        # print(envido)
        return envido


def tiene_31_envido(cartas):
    return calcular_envido(cartas) == 31


def tiene_32_envido(cartas):
    return calcular_envido(cartas) == 32


def tiene_33_envido(cartas):
    return calcular_envido(cartas) == 33


def calcular_probabilidad():
    N = 10000000
    G = sum([tiene_31_envido(repartir_cartas()) for i in range(N)])
    prob = G/N
    print()
    print(f'Tiré {N} veces, de las cuales {G}')
    print(f'Podemos estimar la probabilidad es {prob:.6f}.')


if __name__ == '__main__':
    calcular_probabilidad()
