import preproccessing
import postproccessing
import embedding
import lib


def main():
    # Generate random grayscale image #
    # data = lib.random_grayscale_data(8)
    # postproccessing.data_to_image(data, 'test.png')

    # Use existent image to get data #
    data = preproccessing.image_to_data('test.png')

    # Generate watermark image #
    # embedding.watermark_image(lib.random_watermark_data())

    # TODO: Split data array to 8x8 sub-arrays
    # Split data array to 8x8 sub-arrays #
    # splitted_data = preproccessing.split_data(data)

    # Calculate IWT coefficients #
    coeffs = embedding.iwt2(data)

    # TODO: Check expansibility

    # TODO: Embed watermarking bits

    # Calculate IIWT to get new data array #
    inverse_coeffs = embedding.iiwt2(coeffs)

    # TODO: Combine 8x8 sub-arrays to new data array
    # new_data = postproccessing.merge_data(splitted_data)

    # print("DATA: " + str(data))
    # print("\nSPLITTED DATA: " + str(splitted_data))
    print("\nIWT: " + str(coeffs))
    # print("\nExpansion: " + str(expansion))
    # print("\nEquality: " + str(inverse_coeffs == data))

    # Generate new image from new data array #
    # postproccessing.data_to_image(new_data, 'test_wm.png')


if __name__ == "__main__":
    main()
