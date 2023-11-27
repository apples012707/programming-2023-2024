# Cookies
# Author:
# 21 November 2023

import turtle

# Make baker turtle
baker_turtle = turtle.Turtle()
baker_turtle.color("brown")

# Draw outline of cookie
baker_turtle.penup()
baker_turtle.goto(-5, -30)
baker_turtle.pendown()
baker_turtle.circle(30)
baker_turtle.penup()

# Add five chips
baker_turtle.color("brown")

def make_cookie(x: int, y: int):
    """Draws a cookie on the screen at (x,y)
    
    Params:
    x - x-coodinate of the ccentre of cookie
    y - y-coordinate of the centre of cookie
    """
    # Set up the outline of the cookie
    baker_turtle.color("brown")
    baker_turtle.penup()
    baker_turtle.goto(-5 + x, -30 + y)



#center
baker_turtle.goto(0,0)
baker_turtle.stamp()


# Top Right chip, top left chip, bottom right, bottom left
baker_turtle.goto(10,10)
baker_turtle.stamp()
baker_turtle.goto(-10,-10)
baker_turtle.stamp()
baker_turtle.goto(10,-10)
baker_turtle.stamp()
baker_turtle.goto(-10,10)
baker_turtle.stamp()






turtle.done()