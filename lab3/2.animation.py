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

for i in range (10000000000000):
    r_earth_mars=((xe-xm)**2+(ye-ym)**2)**0.5
    r_earth_venus=((xe-xv)**2+(ye-yv)**2)**0.5
    r_mars_venus=((xm-xv)**2+(ym-yv)**2)**0.5

    f_earth_venus_x= (g*mass_of_earth*mass_of_venus/r_earth_venus**3)*(xv-xe)
    f_earth_mars_x=(g*mass_of_earth*mass_of_mars/r_earth_mars**3)*(xm-xe)
    f_earth_venus_y= (g*mass_of_earth*mass_of_venus/r_earth_venus**3)*(yv-ye)
    f_earth_mars_y=(g*mass_of_earth*mass_of_mars/r_earth_mars**3)*(ym-ye)


    xe=xe+uex*t
    ye=ye+uey*t

    dxe=uex*t
    dye=uey*t

    earth.move(dxe, dye)

    aex=(f_earth_venus_x+f_earth_mars_x)/mass_of_earth
    aey=(f_earth_venus_y+f_earth_mars_y)/mass_of_earth

    uex=uex+aex*t
    uey=uey+aey*t



    f_mars_venus_x= (g*mass_of_mars*mass_of_venus/r_mars_venus**3)*(xv-xm)
    f_mars_earth_x=-1*f_earth_mars_x
    f_mars_venus_y= (g*mass_of_mars*mass_of_venus/r_mars_venus**3)*(yv-ym)
    f_mars_earth_y=-1*f_earth_mars_y
    
    xm=xm+umx*t
    ym=ym+umy*t
    
    dxm=umx*t
    dym=umy*t
    
    mars.move(dxm, dym)

    amx=(f_mars_venus_x+f_mars_earth_x)/mass_of_mars
    amy=(f_mars_venus_y+f_mars_earth_y)/mass_of_mars

    umx=umx+amx*t
    umy=umy+amy*t
    

    f_venus_mars_x=-1*f_mars_venus_x
    f_venus_earth_x=-1*f_earth_venus_x
    f_venus_mars_y=-1*f_mars_venus_x
    f_venus_earth_y=-1*f_earth_venus_y



    xv=xv+uvx*t
    yv=yv+uvy*t

    dxv=uvx*t
    dyv=uvy*t

    venus.move(dxv, dyv)
    
    avx=(f_venus_mars_x+f_venus_earth_x)/mass_of_venus
    avy=(f_venus_mars_y+f_venus_earth_y)/mass_of_venus

    uvx=uvx+avx*t
    uvy=uvy+avy*t

    





