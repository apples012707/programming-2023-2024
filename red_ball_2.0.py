# Centre Red Ball
# Author: Amelia
# Date: Jan 12 2024

# Task: find centre of red ball
import math
from PIL import Image
import red_ball_colour_helper
red_ball_img  = Image.open("./Images/Red Ball.jpeg")
img_mtx = red_ball_img.load()

RED_PIXEL = (160, 0, 0)


red_pixels = []

# Visit every pixel in the image
for y in range(red_ball_img.height):
    for x in range(red_ball_img.width):
        
        current_pixel = red_ball_img.getpixel((x, y))
     
        if red_ball_colour_helper.pixel_to_name(current_pixel) == "red":
            red_pixels.append((x, y))

    current_pixel = img_mtx[x, y]  
    if red_ball_colour_helper.pixel_to_name(current_pixel) == "red":
            red_pixels.append((x, y))

# Create a map of all red pixels "found"
# Create a new image that stores the map
#   - the new image should be the same size as original         
orig_image_width = red_ball_img.width
orig_image_height = red_ball_img.height
red_ball_map = Image.new("RGB", (orig_image_width, orig_image_height))

for pixel_loc in red_pixels:
    red_ball_map(pixel_loc, RED_PIXEL)

# Save the image
red_ball_map.save("./Images/red_ball_map.jpg")
red_ball_map.close()

def find_center():
    img = Image.open("./Images/Red Ball.jpeg")
    img_mtx = img.load()

red_ball_img = img_mtx
current_pixel = img_mtx[x, y]

min_y = max_y = 0
row_0 = True

red_pixel = current_pixel[0]
green_pixel = current_pixel[1]
blue_pixel = current_pixel[2]

for x_axis in range(orig_image_width):
    for y_axis in range(orig_image_height):
        if img_mtx.getpixel((x_axis, y_axis))[0:3] != (255, 255, 255):
            min_y = x_axis
            if row_0:
                max_y = x_axis
                row_0 = False
middle_x_axis = (min_y + max_y) / 2  
    
    
min_x = max_x = 0
column_0 = True
   
   
for y_axis in range(orig_image_height):
        if img_mtx [middle_x_axis, y_axis][0:3] != (255, 255, 255):
            min_x = y_axis
            if column_0:
                max_x = y_axis
                column_0 = False
middle_y_axis = (min_x + max_x) / 2     
   
   
print (middle_y_axis, middle_x_axis)
    
print(find_center())


# Create a map of all red pixels "found"
# Create a new image that stores the map
#   - the new image should be the same size as original

#image_path = "Users/at000097/Programming 2023-24/slss programming/Images/red_ball_map.jpg/" 
#image = Image.open(image_path)

#total_pixels = red_ball_img.width * red_ball_img.height
#radius = math.sqrt(red_pixel_count) / math.pi

#number = radius

# Round to two decimal places
#radius = round(number, 2)
# Generate the report
#print(f"Red pixel: {red_pixel_count}")
#print (f"The centre of the red ball is {radius}")

#cur_x = 1
#x_min = 170
#x_max = 295

# For every pixel location in the red_pixels list
# Place a red pixel at that location
#for pixel_loc in red_pixels:
    #if cur_x < x_min:
        #x_min = cur_x
    #elif cur_x > x_max:
     #x_max = cur_x
#else:
    #print("unknown")



