import preproccessing
import numpy as np
import postproccessing
import embedding
import encoding
import payload_generator as pg
import stats
import plots
import math
import lib
import os
import time

from PIL import Image


def main():
    # Watermarking constants (seem useless)
    alpha = 255
    beta = 0

    path = "img\\test\\"

    for folder in os.listdir(path):

        # Get image (0 - original, 1 - watermarked, 2 - extracted from wmed)
        image = path + folder + "\\" + folder
        names = lib.get_image_names_from(image)

        # Generating payload
        payload_text = pg.text(7500)
        payload = encoding.text_to_bits_unified(payload_text)

        # Embedding
        start_time = time.time()
        key = embed(names[0], payload, alpha, beta)
        embedding_time = time.time() - start_time

        # Extracting
        start_time = time.time()
        watermark = extract(names[1], key)
        exctracting_time = time.time() - start_time

        # Results
        result_pd_len = "Payload bits length: " + str(len(payload))
        result_pd = "Payload text: \n" + payload_text
        result_wm = "Extracted watermark: \n" + str(encoding.bits_to_text_unified(watermark))
        result_eq = "Payload equals to extracted wm (bits): " + str(payload == watermark)
        result_sim = stats.get_similarity(names[0], names[2])
        result_psnr = stats.get_psnr(names[0], names[1])
        result_wm_len = "Extracted watermark bits length: " + str(len(watermark))
        emb_time = "Embedding time: %s s." % embedding_time
        ext_time = "Extraction time: %s s." % exctracting_time
        print(result_eq)
        print(result_sim)
        lib.write_stats(image, result_pd_len, result_wm_len, result_pd, result_wm, result_eq, result_sim, result_psnr, emb_time, ext_time)

        hist_name = image + "_hist.png"
        # plots.histogram(hist_name, names[0], names[2])


def embed(image, payload, alpha=255, beta=0, crop_size=8):
    key = []
    payload = iter(payload)

    # Create filename for restored image
    watermarked_image = image.split(".")[0] + "_wm." + image.split(".")[1]

    # Get image pixels and number of squares
    image_o = Image.open(image).convert('L')
    w, h = image_o.size
    squares = w // crop_size

    # Set array for watermarked image
    data_wm = np.empty((w, h), dtype=int)

    # Processing each block
    for x in range(squares):
        for y in range(squares):
            # Get wavelet coefficients of actual block
            cropped = image_o.crop((x * crop_size, y * crop_size, (x + 1) * crop_size, (y + 1) * crop_size))
            data = preproccessing.crop_to_data(cropped)
            coeffs_orig = embedding.iwt2(data)
            # print("COEFFS: \n", coeffs_orig)

            # Get ll and hh coeffs
            ll = embedding.get_ll(coeffs_orig)
            hh = embedding.get_hh(coeffs_orig)

            # Check if ll in limits
            in_limits = embedding.check_limits(ll, alpha, beta)

            # Check if hh block expansible
            if in_limits:
                expansible = embedding.check_block_expansibility(hh, ll)
            else:
                expansible = False
            # print("Block expansibility: %s" % (str(expansible)))

            # Expand hh coeffs if block expansible, lsb hh coeffs with payload bits and generate key
            if expansible:
                try:
                    new_coeffs = [[embedding.expand(coeffs_orig[r][c], next(payload)) for c in range(4, 8)] for r in
                                  range(4, 8)]
                    key.append(1)
                except StopIteration:
                    key.append(0)
                    new_coeffs = [[coeffs_orig[r][c] for c in range(4, 8)] for r in range(4, 8)]
                new_coeffs = np.array(new_coeffs)
                coeffs_orig = np.array(coeffs_orig)

                # Copy new hh coeffs to all coeffs array
                x1, y1 = (4, 4)
                coeffs_orig[x1:, y1:] = new_coeffs
                # print("NEW COEFFS: \n", coeffs_orig)
            else:
                key.append(0)

            # Get watermarked pixels values
            inverse_coeffs = embedding.iiwt2(coeffs_orig)
            data_wm[y * crop_size: (y + 1) * crop_size, x * crop_size: (x + 1) * crop_size] = inverse_coeffs

    # Get watermarked image
    postproccessing.data_to_image(data_wm, watermarked_image)

    return key


def extract(image, key, crop_size=8):
    hidden = ''

    # Create filename for restored image
    restored_image = image.split(".")[0] + "_ext." + image.split(".")[1]

    # Get image pixels and number of squares
    image_wm = Image.open(image).convert('L')
    w, h = image_wm.size
    squares = w // crop_size

    # Set array for restored image
    data_restored = np.empty((w, h), dtype=int)

    # Iterate the key
    location_i = iter(key)

    # Processing each block
    for x in range(squares):
        for y in range(squares):
            # Get wavelet coefficients of actual block
            cropped = image_wm.crop((x * crop_size, y * crop_size, (x + 1) * crop_size, (y + 1) * crop_size))
            data = preproccessing.crop_to_data(cropped)
            coeffs_wm = embedding.iwt2(data)

            # Get hidden data if block was expanded and set coeffs to original values
            if next(location_i):
                for r in range(4, 8):
                    for c in range(4, 8):
                        hidden += bin(coeffs_wm[r][c])[-1]
                        coeffs_wm[r][c] = math.floor(coeffs_wm[r][c] / 2)

            # Get restored image pixels from wavelet coeffs
            inverse_coeffs = embedding.iiwt2(coeffs_wm)
            data_restored[y * crop_size: (y + 1) * crop_size, x * crop_size: (x + 1) * crop_size] = inverse_coeffs

    # Get restored image
    postproccessing.data_to_image(data_restored, restored_image)

    return hidden


if __name__ == "__main__":
    main()
