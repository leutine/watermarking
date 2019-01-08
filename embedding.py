import numpy as np
import lib
from PIL import Image


def watermark_image(data, path='wm.png'):
    data = list(lib.format_to_1d(np.array(data).tolist()))
    size = int(len(data) ** (1 / 2.0))
    image = Image.new('1', (size, size))
    image.putdata(data)
    image.save(path)
    return True


def check_expansibility(low, high):
    b0 = 0
    b1 = 1

    low = np.array(low).tolist()
    high = np.array(high).tolist()

    result = []

    for i in range(len(low)):
        if abs(2*high[i] + b0) <= min(2*(255-low[i]), 2*low[i] + 1) and \
                abs(2*high[i] + b1) <= min(2*(255-low[i]), 2*low[i] + 1):
            result.append(str(low[i]) + " " + str(high[i]) + " " + str(True))
        else:
            result.append(str(low[i]) + " " + str(high[i]) + " " + str(False))
    print(result)
    return result

    # return np.logical_and(abs(2*high + b0) <= min(2*(255-low), 2*low + 1),
    #                       abs(2*high + b1) <= min(2*(255-low), 2*low + 1))


def iwt(array):
    output = np.zeros_like(array)
    expansion = np.zeros_like(array)
    nx, ny = array.shape
    x = nx // 2
    for j in range(ny):
        low = (array[0::2, j] + array[1::2, j])//2
        high = array[0::2, j] - array[1::2, j]
        output[0:x, j] = low
        output[x:nx, j] = high
        np.append(expansion, check_expansibility(low, high))
    return output


def iiwt(array):
    output = np.zeros_like(array)
    nx, ny = array.shape
    x = nx // 2
    for j in range(ny):
        output[0::2, j] = array[0:x, j] + (array[x:nx, j] + 1)//2
        output[1::2, j] = output[0::2, j] - array[x:nx, j]
    return output


def iwt2(array):
    return iwt(iwt(array.astype(int)).T).T


def iiwt2(array):
    return iiwt(iiwt(array.astype(int).T).T)


def get_ll(coeffs):
    coeffs = np.array(coeffs).tolist()
    output = [row[0:4] for row in coeffs[0:4]]
    return np.array(output)


def get_lh(coeffs):
    coeffs = np.array(coeffs).tolist()
    output = [row[4:] for row in coeffs[0:4]]
    return np.array(output)


def get_hl(coeffs):
    coeffs = np.array(coeffs).tolist()
    output = [row[0:4] for row in coeffs[4:]]
    return np.array(output)


def get_hh(coeffs):
    coeffs = np.array(coeffs).tolist()
    output = [row[4:] for row in coeffs[4:]]
    return np.array(output)
