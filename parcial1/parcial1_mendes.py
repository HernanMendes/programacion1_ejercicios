import csv
import matplotlib.pyplot as plt


def leer_temperaturas(archivo):
    temperaturas = []

    with open(archivo, encoding='utf-8') as file:
        rows = csv.reader(file)
        headers = next(rows)

        for row in rows:
            row[0] = int(row[0])
            row[1:] = [float(i) for i in row[1:]]
            registro = dict(zip(headers, row))
            temperaturas.append(registro)

    return temperaturas


def temps_ciudad(temps, ciudad):
    return [float(temp[ciudad]) for temp in temps]


def temp_promedio_ciudad(temps, ciudad):
    temperaturas_ciudad = temps_ciudad(temps, ciudad)
    return (sum(temperaturas_ciudad)/len(temperaturas_ciudad))


def ultimo_fresco(temps, ciudad):
    promedio = temp_promedio_ciudad(temps, ciudad)
    for temp in temps[::-1]:
        if temp[ciudad] <= promedio:
            return temp['dt']


def reporte_frescores(archivo):
    temperaturas = leer_temperaturas(archivo)
    ciudades = list(temperaturas[0].keys())[1:]

    for ciudad in ciudades:
        ultimo_anio = ultimo_fresco(temperaturas, ciudad)
        print(f"Último año fresco en {ciudad} es: {ultimo_anio}")


def plotear_temps(temps, ciudad):
    anios = [temp['dt'] for temp in temps]
    temperaturas_ciudad = temps_ciudad(temps, ciudad)
    plt.plot(anios, temperaturas_ciudad)
    plt.xlabel('Año')
    plt.ylabel('Temperatura')
    plt.title(f"Evolución de la temperatura en la ciudad de {ciudad}")
    plt.show()


def main():
    archivo = './temperaturas.csv'
    ciudad = 'Montevideo'
    temperaturas = leer_temperaturas(archivo)
    temperaturas_ciudad = temps_ciudad(temperaturas, ciudad)
    temperatura_promedio_ciudad = temp_promedio_ciudad(temperaturas, ciudad)
    ultima_anio_fresco = ultimo_fresco(temperaturas, ciudad)
    reporte = reporte_frescores(archivo)
    plotear_temps(temperaturas, ciudad)


if __name__ == '__main__':
    main()
