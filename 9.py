import turtle
import math


x=5
i=3
R=30
a=R
k=0
turtle.shape('turtle')
while i<13:
    turtle.left(180-(180*(i-2)/i)*0.5)
    while k<i:
        c=a*2*math.sin(((2*math.pi)/(i*2)))
        turtle.forward(c)
        turtle.left(180-(180*(i-2)/i))
        k+=1
    k=0
    turtle.right(180-(180*(i-2)/i)*0.5)
    turtle.penup()
    turtle.forward(R)
    a+=R
    i+=1
    turtle.pendown()
    
    
