# Colour Helper
# Functions that help wither colours


def is_light(pixel: tuple) -> bool:
    """Returns True if the pixel is a "light" pixel

    Params:
        pixel - 3-tuple of values r, g, b

    Returns:
        True if the pixel is a light pixel
        False if a dark pixel
    """
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]

    average = (red + green + blue) / 3

    if average >= 128:
        return True
    else:
     return False