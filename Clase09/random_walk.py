import numpy as np
import matplotlib.pyplot as plt
import math


def randomwalk(largo):
    pasos = np.random.randint(-1, 2, largo)
    return pasos.cumsum()


def plot_together(n_walks, largo, colors):
    fig = plt.figure()
    plt.subplot(2, 1, 1)
    plt.grid()
    plt.title('12 Caminatas al azar')
    plt.xlabel('Tiempo')
    plt.ylabel('Distancia al origen')

    distancia_max = 0
    distancia_min = math.inf
    walk_max = None
    walk_min = None
    color_max = None
    color_min = None
    for i in range(n_walks):
        walk = randomwalk(largo)
        plt.plot(walk, color=colors[i])

        max_dist = np.max(np.abs(walk))

        if max_dist > distancia_max:
            distancia_max = max_dist
            walk_max = walk
            color_max = colors[i]

        if max_dist < distancia_min:
            distancia_min = max_dist
            walk_min = walk
            color_min = colors[i]

    plt.subplot(2, 2, 3)
    plt.title('La caminata que mas se aleja')
    plt.grid()
    plt.plot(walk_max, color=color_max, label='Distancia máxima')
    plt.xlabel('Tiempo')
    plt.ylabel('Distancia al origen')

    plt.subplot(2, 2, 4)
    plt.title('La caminata que menos se aleja')
    plt.grid()
    plt.plot(walk_min, color=color_min, label='Distancia mínima')
    plt.xlabel('Tiempo')
    plt.ylabel('Distancia al origen')
    plt.show()


if __name__ == '__main__':
    n_walks = 12
    largo = 100000
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'orange', 'purple', 'brown', 'pink', 'gray']
    plot_together(n_walks, largo, colors)
