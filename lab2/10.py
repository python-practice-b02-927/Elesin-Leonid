import turtle

turtle.shape('turtle')
i=0
k=0
turtle.speed (1)
while k<3:
    while i<1000:
        turtle.forward(1)
        turtle.left (360/1000)
        i+=1
    i=0
    while i<1000:
        turtle.forward(1)
        turtle.right (360/1000)
        i+=1
    i=0
    turtle.left (60)
    k=k+1


    
input() 
