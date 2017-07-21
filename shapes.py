from turtle import *
import math

# Name your Turtle.
t = Turtle()

# Set Up your screen and starting position.
t.penup()
setup(500,300)
x_pos = 0
y_pos = 0
t.setposition(x_pos, y_pos)

### Write your code below:

t.pendown()
t.forward(100)
t.right(90)
#t.penup()
t.forward(100)
t.left(90)
t.backward(100)
t.left(90)
t.forward(100)

exitonclick()
