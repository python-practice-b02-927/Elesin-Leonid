import graphics as gr
window = gr.GraphWin("Jenkslex and Ganzz project", 1000, 1000)
nebo=gr.Rectangle(gr.Point(0, 0), gr.Point(1000, 500))
nebo.setFill('blue')
zemelya=gr.Rectangle(gr.Point(0, 500), gr.Point(1000, 1000))
zemelya.setFill('green')
dom=gr.Rectangle(gr.Point (50, 400), gr. Point (450, 600))
dom.setFill('sienna4')
krishadoma=gr.Polygon(gr.Point (50, 400), gr.Point (450, 400), gr.Point (250, 300))
krishadoma.setFill('salmon4')
solntse=gr.Circle(gr.Point(800, 100), 80)
solntse.setFill('orange')
obl=gr.Circle(gr.Point(100, 150), 60)
obl.setFill('white')
obl2=gr.Circle(gr.Point(130, 150), 60)
obl2.setFill('white')
obl3=gr.Circle(gr.Point(160, 150), 60)
obl3.setFill('white')
obl4=gr.Circle(gr.Point(190, 150), 60)
obl4.setFill('white')
obl5=gr.Circle(gr.Point(220, 150), 60)
obl5.setFill('white')
obl6=gr.Circle(gr.Point(130, 110), 60)
obl6.setFill('white')
obl7=gr.Circle(gr.Point(180, 110), 60)
obl7.setFill('white')
obl8=gr.Circle(gr.Point(400, 150), 60)
obl8.setFill('white')
obl9=gr.Circle(gr.Point(430, 150), 60)
obl9.setFill('white')
obl10=gr.Circle(gr.Point(460, 150), 60)
obl10.setFill('white')
obl11=gr.Circle(gr.Point(490, 150), 60)
obl11.setFill('white')
obl12=gr.Circle(gr.Point(420, 150), 60)
obl12.setFill('white')
obl13=gr.Circle(gr.Point(430, 110), 60)
obl13.setFill('white')
obl14=gr.Circle(gr.Point(480, 110), 60)
obl14.setFill('white')
molnya=gr.Polygon(gr.Point(200, 210), gr.Point(220, 210), gr.Point (240,250), gr.Point(220, 290), gr.Point(220, 330), gr.Point (200, 290), gr.Point (220, 250))
molnya.setFill('yellow')
reka=gr.Polygon(gr.Point(1000, 500), gr.Point (800, 500), gr.Point (0,1000), gr.Point(200, 1000))
reka.setFill('cyan')

nebo.draw(window)
zemelya.draw(window)
dom.draw(window)
krishadoma.draw(window)
solntse.draw(window)
obl.draw(window)
obl2.draw(window)
obl3.draw(window)
obl4.draw(window)
obl5.draw(window)
obl6.draw(window)
obl7.draw(window)
obl8.draw(window)
obl9.draw(window)
obl10.draw(window)
obl11.draw(window)
obl12.draw(window)
obl13.draw(window)
obl14.draw(window)
molnya.draw(window)
reka.draw(window)
window.getMouse()
window.getClose()
