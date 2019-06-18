import numpy as np


def format_to_1d(data):
    return np.array(data).flatten()


def format_to_2d(data, col=8):
    # data = [data[offset:offset + width] for offset in range(0, width * height, width)]
    # return list(data)

    return np.array(data).reshape((-1, col))


def get_image_names_from(image):
    image_orig = "%s.png" % image
    image_wm = "%s_wm.png" % image
    image_ext = "%s_wm_ext.png" % image
    return [image_orig, image_wm, image_ext]


def write_stats(image, *stats):
    filename = "stats\\" + image.split("\\")[-1] + ".txt"
    file = open(filename, "w+")

    file.write(image + "\n")
    for stat in stats:
        file.write(stat + "\n")

    file.close()
