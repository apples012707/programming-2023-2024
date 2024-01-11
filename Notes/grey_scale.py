def picture_to_greyscale(filename: str) -> None:
    """ Convert a gvien picture to greyscale"""


# Open up the image
with Image.open(f"./Image/{filename}") as im:
    # Visit every pixel
    for y in range(im.height):
        for x in range(im.wideth):
            pixel - im.getpixel((x,y))

            # Take that pixel and convert it to grey
            grey_pixel = coloour_helper.pixel_to_greyscale(pixel)

            pixel = im.putpixel((x,y))

            # Take that pixel and randomize it
            random_pixel = colour_helper_pixel_to_random_effect(pixel)
# Save the image