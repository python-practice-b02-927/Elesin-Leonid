import turtle

turtle.shape('turtle')

def quadrat():
    i=0
    while i<4:
        turtle.forward(d)
        turtle.left (90)
        i+=1
    
n=100
k=1
f=0
while f<10:
    d=k*n
    quadrat()
    turtle.penup()
    turtle.right(90)
    turtle.forward(n)
    turtle.right(90)
    turtle.forward(n)
    turtle.right(180)
    turtle.pendown()
    k+=2
    f+=1
      
    
    
    

    


    
