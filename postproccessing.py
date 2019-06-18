import lib
import numpy as np
from PIL import Image


def data_to_image(data, path='wm.png'):
    data = list(lib.format_to_1d(np.array(data).tolist()))
    try:
        size = int(len(data) ** (1/2.0))
    except ValueError as e:
        raise AssertionError("Не удалось вычислить размер массива данных изображения!\nException: " + str(e))
    image = Image.new('L', (size, size))
    image.putdata(data)
    image.save(path, "PNG")
    return True

