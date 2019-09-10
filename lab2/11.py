import turtle

turtle.shape('turtle')
i=0
k=0
turtle.speed (1)
turtle.left(90)
N=100
while N<1000:
    while i<N:
        turtle.forward(1)
        turtle.left (360/N)
        i+=1
    i=0
    while i<N:
        turtle.forward(1)
        turtle.right (360/N)
        i+=1
    i=0
    k=k+1
    N=N+50


    
input() 
