import random
from collections import Counter


def definir_cumples(cant_personas):
    return [random.randint(1, 365) for i in range(cant_personas)]


def hay_cocumple(cumples):
    contador = Counter(cumples)
    if contador.most_common(1)[0][1] >= 2:
        return True
    return False


def main():
    cant_personas = 23
    cumples = definir_cumples(cant_personas)
    return hay_cocumple(cumples)


def calcular_probabilidad():
    N = 1000000
    G = sum([main() for i in range(N)])
    prob = G/N
    print()
    print(f'Tiré {N} veces, de las cuales {G} hay cocumple')
    print(f'Podemos estimar la probabilidad de que haya cocumple mediante {prob:.6f}.')


if __name__ == '__main__':
    calcular_probabilidad()


# La probabilidad de que haya cocumple en 30 personas en aprox 0.7
# Para que la probabilidad sea aprox 0.5 debe ser un grupo de 23 personas
