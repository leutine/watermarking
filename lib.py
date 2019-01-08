import random
import numpy as np


def random_grayscale_data(size=16):
    data = [[random.randint(0, 255) for i in range(size)] for j in range(size)]
    data = np.array(data)
    return data


def random_watermark_data(size=4):
    data = [[random.randint(0, 1) for i in range(size)] for j in range(size)]
    data = np.array(data)
    return data


def format_to_1d(data):
    # for element in data:
    #     if type(element) in (tuple, list):
    #         for item in format_to_1d(element):
    #             yield item
    #     else:
    #         yield element

    return np.array(data).flatten()


def format_to_2d(data, col=8):
    # data = [data[offset:offset + width] for offset in range(0, width * height, width)]
    # return list(data)

    return np.array(data).reshape((-1, col))

