 
# Pumpkin Drawing
# Author: Amelia Tang
# Date: 31 October 2023

import turtle
import time
window = turtle.Screen()
window.bgcolor("purple")
# Whole pumpkin
pumpkin = turtle.Turtle()
pumpkin.hideturtle()
pumpkin.color("orange")
pumpkin.dot(300)
# The turtle to "carve" the pumpkin
carver = turtle.Turtle()
# "Flatten" the lower part of the pumpkin
carver.penup()
carver.setposition(-300, -150)
carver.pensize(30)
carver.pendown()
carver.forward(600)
carver.pensize(2)
# Left eye
carver.penup()
carver.setposition(-50, -5)
carver.pendown()
carver.fillcolor("black")
carver.begin_fill()
carver.circle(30)
carver.end_fill()
carver.penup()
# Right eye
carver.penup()
carver.setposition(50, -5)
carver.pendown()
carver.fillcolor("black")
carver.begin_fill()
carver.circle(30)
carver.end_fill()
carver.penup()


# Mouth
carver.penup()
carver.setposition(10, -30)

carver.right(90)
carver.goto(-50, -50)   # Move to the starting point of the mouth
carver.begin_fill()    # Start filling the shape
carver.circle(50, 180)  # Draw a semi-circle for the mouth
carver.end_fill()      # End the filling
carver.penup()


# Nose
carver.penup()
carver.setposition(20, -20)
carver.pendown()
carver.fillcolor("black")
carver.begin_fill()
carver.circle(20)
carver.end_fill()
carver.penup()



# cheeks left
carver.penup()
carver.setposition(-70, -20)
carver.pendown()
carver.fillcolor("black")
carver.begin_fill()
carver.circle(10)
carver.end_fill()
carver.penup()


# Cheeks right
carver.penup()
carver.setposition(100, -20)
carver.pendown()
carver.fillcolor("black")
carver.begin_fill()
carver.circle(10)
carver.end_fill()
carver.penup()

turtle.done()