import turtle
import math


def mnogoug():
    for k in range(i):
        c=a*2*math.sin(((2*math.pi)/(i*2)))
        turtle.forward(c)
        turtle.left(180-(180*(i-2)/i))

        
i=3
R=30
a=R
turtle.shape('turtle')
for i in range (3, 13):
    turtle.left(180-(180*(i-2)/i)*0.5)
    mnogoug()
    turtle.right(180-(180*(i-2)/i)*0.5)
    turtle.penup()
    turtle.forward(R)
    a+=R
    i+=1
    turtle.pendown()
    
       
