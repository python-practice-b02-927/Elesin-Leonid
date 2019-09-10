import turtle
import math
n=5
i=0
while i<5:
    turtle.forward(100)
    turtle.left(180-180/n)
    i+=1
    
turtle.penup()
turtle.goto(200, 0)
i=0
n=11
turtle.pendown()
while i<11:
    turtle.forward(100)
    turtle.left(180-180/n)
    i+=1

