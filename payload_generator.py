import numpy as np
import random
import string
from PIL import Image


def image_bw(path="payload.png", size=30):
    array = np.random.randint(2, size=(size, size))
    print(array)
    image = Image.fromarray(array.astype('uint32'), '1')
    image.save(path)
    return True


def text(length=50):
    return "".join([random.choice(string.ascii_letters) for i in range(length)])


