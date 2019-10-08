import graphics as gr
window = gr.GraphWin("3 bodies problem", 1000, 1000)
space=gr.Rectangle(gr.Point(0,0), gr.Point(1000,1000))
space.setFill('black')
space.draw(window)


"""Determine fundamental constants"""
mass_of_earth=100
mass_of_venus=20000
mass_of_mars=100
g=0.05
t=0.01


"""Determine initial conditions"""
xe=500
ye=700
uex=1
uey=0
xv=500
yv=300
uvx=0
uvy=0
xm=500
ym=500
umx=2
umy=0


"""Draw bodies"""
earth = gr.Circle(gr.Point(xe,ye), 10)
earth.setFill('blue')
earth.draw(window)


mars = gr.Circle(gr.Point(xm,ym), 10)
mars.setFill('red')
mars.draw(window)

 
venus = gr.Circle(gr.Point(xv,yv), 10)
venus.setFill('yellow')
venus.draw(window)


    
    





