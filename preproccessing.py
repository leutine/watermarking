import lib
import numpy as np
from PIL import Image


def image_to_data(path='img\\orig\\lena.jpg'):
    # convert image to 8-bit grayscale
    img = Image.open(path).convert('L')

    # get image's size
    width, height = img.size

    # convert image data to a list of integers
    data = list(img.getdata())

    # convert that to 2D list (list of lists of integers)
    data = lib.format_to_2d(data, width)

    # Another method (native python) #
    # data = [data[offset:offset + width] for offset in range(0, width * height, width)]

    # return data 2D list
    return data


def split_data(data, size=8):
    # Not working! #
    # num = int((data.size / size ** 2))
    # nr = data.shape[0]  # number of rows
    # nc = data.shape[1]  # number of columns
    # sub_arrays = np.zeros((num, size, size), dtype=np.int_)
    # L1 = data[:size, :size]
    # L2 = data[:size, size:nc]
    # L3 = data[size:nr, :size]
    # L4 = data[size:nr, size:nc]
    # sub_arrays[0] = L1
    # for i in sub_arrays:
    #     sub_arrays[i]

    # Working method #
    crop = [data[x:x + size, y:y + size] for x in range(0, data.shape[0], size) for y in range(0, data.shape[1], size)]
    crop = np.array(crop)

    return crop
