import numpy as np
import math

from PIL import Image


def diff(image1, image2, simplified=True):
    image1 = Image.open(image1).convert('L')
    image2 = Image.open(image2).convert('L')

    data1 = np.asarray(image1)
    data2 = np.asarray(image2)

    if simplified:
        return np.array_equal(data1.flatten(), data2.flatten())
    else:
        return np.array(data1 == data2)


def similarity(image1, image2):
    result = diff(image1, image2, simplified=False).flatten()
    return (result == True).sum() / len(result) * 100


def psnr(image1, image2):
    image1 = Image.open(image1).convert('L')
    image2 = Image.open(image2).convert('L')

    data1 = np.asarray(image1)
    data2 = np.asarray(image2)

    mse = np.mean((data1.flatten() - data2.flatten()) ** 2)
    if mse == 0:
        return 100

    return 20 * math.log10(255 / math.sqrt(mse))


def get_similarity(image1, image2):
    return "Similarity (original <> extracted): " + str(similarity(image1, image2))


def get_psnr(image1, image2):
    return "PSNR (original <> watermarked): " + str(psnr(image1, image2))
