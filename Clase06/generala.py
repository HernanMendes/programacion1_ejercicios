import random
from collections import Counter


def tirar(cant_dados):
    tirada = []
    for i in range(cant_dados):
        tirada.append(random.randint(1, 6))
    return tirada


def es_generala(tirada):
    if len(tirada) == 5:
        numero = tirada[0]
        for dado in tirada[1:]:
            if dado != numero:
                return False
        return True
    else:
        return False


def generala_no_servida(vez):
    dados_guardados = []
    chances = 3
    is_generala = False
    cant_dados = 5
    repeticiones = 0

    while chances > 0 and not is_generala:
        chances -= 1
        tirada = tirar(cant_dados-repeticiones)
        dados_actuales = tirada + dados_guardados
        contador = Counter(dados_actuales)
        cara, repeticiones = contador.most_common(1)[0]

        dados_guardados = []
        for i in range(repeticiones):
            dados_guardados.append(cara)

        is_generala = es_generala(dados_guardados)

        # print(tirada)
        # print(cara, repeticiones)
        # print(dados_guardados)
        # print(is_generala)
        # print()

    print(dados_actuales, end=' ')
    if is_generala:
        print("GENERALA!")
    else:
        print()
    return is_generala


N = 1000000
G = sum([generala_no_servida(i) for i in range(N)])
prob = G/N
print()
print(f'Tiré {N} veces, de las cuales {G} saqué generala')
print(f'Podemos estimar la probabilidad de sacar generala mediante {prob:.6f}.')
