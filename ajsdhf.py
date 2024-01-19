# Centre Red Ball
# Author: Amelia and Ruby
# Date: Jan 12 2024
# Task: find centre of red ball
import math
from PIL import Image
import red_ball_colour_helper
red_ball_img  = Image.open("./Images/Red_Ball.jpeg")
img_mtx = red_ball_img.load()
RED_PIXEL = (160, 0, 0)
red_pixels = []
# Visit every pixel in the image
for y in range(red_ball_img.height):
    for x in range(red_ball_img.width):
        # Get the pixel information
        current_pixel = red_ball_img.getpixel((x, y))
        # Detect the current pixel's colour
        if red_ball_colour_helper.pixel_to_name(current_pixel) == "red":
            red_pixels.append((x, y))
# Create a map of all red pixels "found"
# Create a new image that stores the map
#   - the new image should be the same size as original
orig_image_width = red_ball_img.width
orig_image_height = red_ball_img.height
red_ball_map = Image.new("RGB", (orig_image_width, orig_image_height))
for pixel_loc in red_pixels:
    red_ball_map.putpixel(pixel_loc, RED_PIXEL)
# Save the image
red_ball_map.save("./Images/red_ball_map.jpg")
red_ball_map.close()
red_ball_img = img_mtx
def find_center():
    img = Image.open("./Images/Red Ball.jpeg")
    img_mtx = img.load()
min_y = max_y = 0
row_0 = True
for x_axis in range:
    for y_axis in range:
        if img_mtx[x_axis, y_axis][0:3] != (255, 255, 255):
            min_y = x_axis
            if row_0:
                max_y = x_axis
                row_0 = False
middle_x_axis = (min_y + max_y) / 2
min_x = max_x = 0
column_0 = True
for y_axis in range:
        if img_mtx[middle_x_axis, y_axis][0:3] != (255, 255, 255):
            min_x = y_axis
            if column_0:
                max_x = y_axis
                column_0 = False
middle_y_axis = (min_x + max_x) / 2
print (middle_y_axis, middle_x_axis)
print(find_center())