import lib
import numpy as np
from PIL import Image


def crop_to_data(cropped_image):
    width, height = cropped_image.size
    data = list(cropped_image.getdata())
    data = lib.format_to_2d(data, width)
    return data


def image_to_data(path='img\\test\\lena.png'):
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


def crop(image, size=192):
    cropped_name = image.split(".")[0] + ".png"
    img = Image.open(image).convert('L')
    w, h = img.size
    cropped = img.crop((0, 0, size, size))
    return cropped.save(cropped_name, "PNG")

