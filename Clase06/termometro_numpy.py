import random
import numpy as np

media_error = 0
desvio_error = 0.2
temperatura = 37.5


def medir_temp(n):
    temperaturas = [random.normalvariate(mu=temperatura, sigma=desvio_error) for i in range(n)]
    temp_array = np.array(temperaturas)
    np.save('../Data/temperaturas.npy', temp_array)
    return temperaturas


def resumen_temp(n):
    mediciones = medir_temp(n)
    maximo = max(mediciones)
    minimo = min(mediciones)
    promedio = sum(mediciones)/len(mediciones)
    mediciones.sort()
    # print(mediciones)
    if len(mediciones) % 2 == 0:
        pos = round(len(mediciones)/2)
        mediana = (mediciones[pos]+mediciones[pos-1])/2
    else:
        mediana = mediciones[round(len(mediciones)/2)]
    return maximo, minimo, promedio, mediana


def main():
    n = 999
    maximo, minimo, promedio, mediana = resumen_temp(n)
    print(f"Maximo: {maximo}")
    print(f"Minimo: {minimo}")
    print(f"Promedio: {promedio}")
    print(f"Mediana: {mediana}")


if __name__ == '__main__':
    main()
