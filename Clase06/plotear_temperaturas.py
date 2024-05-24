import numpy as np
import matplotlib.pyplot as plt


def plotear_temperaturas(nombre_archivo):
    temperaturas = np.load(nombre_archivo)
    plt.hist(temperaturas, bins=50)
    plt.show()
    # plt.savefig('./temperaturas.png')


if __name__ == '__main__':
    nombre_archivo = '../Data/temperaturas.npy'
    plotear_temperaturas(nombre_archivo)
