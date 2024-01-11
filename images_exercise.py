# Images Problem
# Author: Amelia
# 18 December 2023


# Open the image

# For every pixel in the image
# if the pixel is light
# replace it with a light pixel
# else
# replace it with a dark pixel

# After visiting every pixel, save the image

from PIL import Image

# open up kid green
with Image.open("./Images/binary-image.png") as im:
    # create variables that store the width and height
    image_height = im.height
    image_width = im.width

    # open background image
    bg_im = Image.open("./Images/binary-image.png")


def is_light(pixel: tuple) -> bool:
    """Returns True if the pixel is a "light" pixel

    Params:
        pixel - 2-tuple of values w, b

    Returns:
        True if the pixel is a light pixel
        False if a dark pixel
    """
    white = pixel[0]
    black = pixel[1]


    average = (white + black) / 2

    if average >= 128:
        return True
    else:
        return False


# Test?
light_pixel = (255, 255, 255)



dark_pixel = (0, 0, 0)

print(is_light(light_pixel))  # True
print(is_light(dark_pixel))  # False