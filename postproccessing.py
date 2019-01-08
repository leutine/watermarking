import lib
import numpy as np
from PIL import Image


def data_to_image(data, path='test_post.png'):
    data = list(lib.format_to_1d(np.array(data).tolist()))
    try:
        size = int(len(data) ** (1/2.0))
    except ValueError as e:
        raise AssertionError("Не удалось вычислить размер массива данных изображения!\nException: " + str(e))
    image = Image.new('L', (size, size))
    image.putdata(data)
    image.save(path)
    return True


def merge_data(sub_arrays):
    # TODO: Make this thing work as intended
    # Как должно работать: на вход подается ТРЕХМЕРНЫЙ массив (n*8*8, где n - количество блоков 8х8),
    # на выходе ДВУХМЕРНЫЙ массив такого размера, как и исходные данные в изображении (возможно придется на вход
    # передавать и их), состоящий из объединенных блоков 8х8 в строгом порядке (пока не ясно точно в каком)

    sub_arrays = np.array(sub_arrays).flatten().reshape((8, 8))
    # Это необязательно
    # data = lib.format_to_2d(sub_arrays)
    data = sub_arrays
    return data
