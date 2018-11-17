from zadA import zad_a
from zadB import zad_b
from zadC import zad_c
import matplotlib
# matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":

    dim = 50
    results = []
    error = []
    for n in range(1, dim):
        a = []
        for i in range(0, 100):
            x = zad_c(n)
            a.append(x)
        results.append(np.mean(a))
        error.append(np.std(a))

    x = range(1, dim)

    plt.rcParams["figure.figsize"] = [16, 12]
    ax = plt.axes()

    ax.set_xlabel('Liczba wymiarow')
    # ax.set_ylabel('Procent punktów w wewnątrz hiperkuli')
    # ax.set_ylabel('Stosunek odchylenia standardowego odległości między punktami do średniej odległości między nimi')
    # średni kąt pomiędzy parą wektorów
    plt.errorbar(x, results, error, marker='o', ecolor='red', elinewidth=2)
    plt.show()


