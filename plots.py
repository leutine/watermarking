import numpy as np
import matplotlib.patches as mpatches

from matplotlib import pyplot as plt
from PIL import Image


def histogram(filename, *images):
    colors = iter(['blue', 'green', 'orange', 'red'])

    for image in images:
        color = next(colors)
        im = Image.open(image).convert('L')
        data = np.asarray(im).flatten()
        plt.hist(data, color=color, label=image, bins=256, alpha=0.5)

    plt.ylabel("Количество пикселей")
    plt.xlabel("Значения пикселей")
    plt.legend(loc=1)

    plt.savefig(filename)
    plt.clf()
    # plt.show()
