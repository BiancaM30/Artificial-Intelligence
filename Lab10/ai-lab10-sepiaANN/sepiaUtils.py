# Sepia is a filter based on exagerating red, yellow and brown tones
# This implementation exagerates mainly yellow with a little brown
from imageUtils import create_image, get_pixel


# Limit maximum value to 255
def get_max(value):
    if value > 255:
        return 255

    return int(value)

def get_sepia_pixel(red, green, blue, alpha):
    # This is a really popular implementation
    tRed = get_max((0.759 * red) + (0.398 * green) + (0.194 * blue))
    tGreen = get_max((0.676 * red) + (0.354 * green) + (0.173 * blue))
    tBlue = get_max((0.524 * red) + (0.277 * green) + (0.136 * blue))

    # Return sepia color
    return tRed, tGreen, tBlue, alpha


# Convert an image to sepia
def convert_sepia(image):
    # Get size
    width, height = image.size

    # Create new Image and a Pixel Map
    new = create_image(width, height)
    pixels = new.load()

    # Convert each pixel to sepia
    for i in range(0, width, 1):
        for j in range(0, height, 1):
            p = get_pixel(image, i, j)
            pixels[i, j] = get_sepia_pixel(p[0], p[1], p[2], 255)

    # Return new image
    return new