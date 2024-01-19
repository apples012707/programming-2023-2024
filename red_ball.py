# Centre Red Ball
# Author: Amelia
# Date: Jan 12 2024

# Task: find centre of red ball
import math
from PIL import Image
import colour_helper
RED_PIXEL = (160, 0, 0)

red_ball_img = Image.open("./Images/Red Ball.jpeg")

red_pixels = []

# Visit every pixel in the image
for y in range(red_ball_img.height):
    for x in range(red_ball_img.width):
        
        # Get the pixel information
        current_pixel = red_ball_img.getpixel((x, y))
        # Detect the current pixel's colour
        if colour_helper.pixel_to_name(current_pixel) == "red":
            red_pixels.append((x, y))


# Create a map of all red pixels "found"
# Create a new image that stores the map
#   - the new image should be the same size as original
            
orig_image_width = red_ball_img.width
orig_image_height = red_ball_img.height
red_ball_map = Image.new("RGB", (orig_image_width, orig_image_height))

# For every pixel location in the red_pixels list
# Place a red pixel at that location

for pixel_loc in red_pixels:
    red_ball_map.putpixel(pixel_loc, RED_PIXEL)

# Save the image
red_ball_map.save("./Images/red_ball_map.jpg")
red_ball_map.close()

# Count all the locations of red pixels
red_pixel_count = len(red_pixels)

total_pixels = red_ball_img.width * red_ball_img.height
radius = math.sqrt(red_pixel_count) / math.pi

number = radius

# Round to two decimal places
radius = round(number, 2)
# Generate the report
print(f"Red pixel: {red_pixel_count}")
print (f"The centre of the red ball is {radius}")


red_ball_img.close()