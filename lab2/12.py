import turtle

turtle.shape('turtle')
i=0
k=0
turtle.left(90)
N=100
while True:
    while i<N:
        turtle.forward(1)
        turtle.right (180/N)
        i+=1
    i=0
    while k<(N/4):
        turtle.forward(1)
        turtle.right (180*4/N)
        k=k+1
    k=0


    
input() 
