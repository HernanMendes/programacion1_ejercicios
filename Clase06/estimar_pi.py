import random


def generar_punto():
    x = random.random()
    y = random.random()
    return x, y


def estimar_pi():
    N = 100000000
    M = 0

    for i in range(N):
        x, y = generar_punto()
        if (x*x + y*y) < 1:
            M += 1

    return 4*M/N


def main():
    pi_estimado = estimar_pi()
    print(f"pi_estimado: {pi_estimado}")


if __name__ == '__main__':
    main()
