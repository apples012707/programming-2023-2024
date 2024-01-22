# Red Ball Colour Helper
# Author; Amelia + Ruby
# Date: Jan 22 2024
# Functions that help wither colours


def pixel_to_name(pixel: tuple) -> str:
    """Given a 3-tuple, return a string representing
    its colour

    Params:
        pixel = 3-tuple of values (red, green, blue)

    Returns:
        name of the colour
    """
    red, green, blue = pixel

    if red > 195 and green < 90 and blue < 90:
        return "red"
    else:
        return "unknown"


print(pixel_to_name((180, 3, 2)))

def is_light(pixel: tuple) -> bool:
    """Returns True if the pixel is a "light" pixel

    Params:
        pixel - 3-tuple of values r, g, b

    Returns:
        True if the pixel is a light pixel
        False if a dark pixel
    """
    red = pixel[0]


def pixel_to_grayscale(pixel: tuple) -> tuple:
    """Return a gray version of the given pixel"""
    red, green, blue = pixel

    gray = int(red * 0.3 + green * 0.59 + blue * 0.11)

    return (gray, gray, gray)


def pixel_to_random_effect(pixel: tuple) -> tuple:
    """Return a random pixel"""
    red, green, blue = pixel

    red += 30
    green += 50
    blue -= 10

    if red > 255:
        red = 255
    if green > 255:
        green = 255
    if blue < 0:
        blue = 0

    return (red, green, blue)