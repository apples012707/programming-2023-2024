# Turtle Example
# Author: Amelia Tang
# Date: Nov. 21. 2023

import turtle

# --- CONSTANTS (doesn't change --> ALL CAPS)
TURTLE_MAGNITUDE = 20

# Create a Turtle
michaelangelo = turtle.Turtle()

# Get some instructions from the user
print ("""To give commands, type:
F - to go forward
L - to go left
R - to go right
B - to go backward
Stop - to stop""")


# Repeat the below code INDEFINITELY
done = False

while not done:
    command = input("where should I go?").strip(",.?!").lower()


# Based on those instructions, move the trutle on the screen
# If the user says stop, quit the loop
    if command in ["f", "forward"]:
        michaelangelo.forward(TURTLE_MAGNITUDE)
    elif command in ["l", "left"]:
        michaelangelo.left(90)
    elif command in ["r", "right"]:
     michaelangelo.right(90)
    elif command in ["b", "backward"]:
        michaelangelo.backward(TURTLE_MAGNITUDE)
    elif command == "stop":
        done = True


