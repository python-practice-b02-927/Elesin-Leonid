import turtle
import math

turtle.shape('turtle')
i=0
k=0
N=1000
turtle.left(90)
turtle.penup()
turtle.goto(N/(2*math.pi), 0)
turtle.pendown()
turtle.speed(1000)
turtle.color("black", "yellow")
turtle.begin_fill()
while i<N:
    turtle.forward(1)
    turtle.left (360/N)
    i+=1
turtle.end_fill()
turtle.penup()
turtle.goto(-1*N/(8*math.pi),N/(math.pi*3))
turtle.pendown()
i=0
turtle.color("black", "blue")
turtle.begin_fill()
while i<(N/10):
    turtle.forward(1)
    turtle.left (3600/N)
    i+=1
i=0
turtle.end_fill()
turtle.penup()
turtle.goto(N/(8*math.pi),N/(math.pi*3))
turtle.pendown()
i=0
turtle.color("black", "blue")
turtle.begin_fill()
while i<(N/10):
    turtle.forward(1)
    turtle.right (3600/N)
    i+=1
turtle.end_fill()
turtle.penup()
turtle.goto(-1*N/(4*math.pi), 0)
turtle.pendown()
turtle.left(180)
i=0
turtle.width(5)
turtle.color('red')
turtle.circle(N/(4*math.pi), 180)








    
input() 
