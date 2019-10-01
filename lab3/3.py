import graphics as gr

    
def draw_mountain_above(win):
    mountain_above = gr.Polygon(gr.Point(20, 390), gr.Point(900, 270),
                                gr.Point(795, 225), gr.Point(750, 250),
                                gr.Point(700, 210 ),gr.Point(650, 220),
                                gr.Point(580,140),gr.Point(570,143),
                                gr.Point(545,180),gr.Point(490,257),
                                gr.Point(454,258),gr.Point(424,283),
                                gr.Point(388,266),gr.Point(352,343),
                                gr.Point(316,312),gr.Point(256,344),
                                gr.Point(149,264),gr.Point(136,238),
                                gr.Point(117,224),gr.Point(98,313),
                                gr.Point(88,328),gr.Point(42,345))
    mountain_above.setFill ('orange')
    mountain_above.setOutline ('orange')
    mountain_above.draw(win)


def draw_mountain_at_the_middle(win):
    mountain_at_the_middle = gr.Polygon(gr.Point(0,416), gr.Point(31,415),
                                        gr.Point(48,432), gr.Point(133,500),
                                        gr.Point(179,444), gr.Point(228,471),
                                        gr.Point(243,390), gr.Point(295,406),
                                        gr.Point(327,450), gr.Point(438,428),
                                        gr.Point(498,362), gr.Point(632,432),
                                        gr.Point(687,383), gr.Point(723,405),
                                        gr.Point(768,375), gr.Point(812,394),
                                        gr.Point(900,303), gr.Point(900,540),
                                        gr.Point(0,540))
    mountain_top=gr.Oval(gr.Point(50, 350), gr.Point(140, 540))
    mountain_top.setFill ('red')
    mountain_top.setOutline('red')
    mountain_top_2=gr.Oval (gr.Point(439,357), gr.Point(525,495))
    mountain_top_2.setFill('red')
    mountain_top_2.setOutline('red')
    mountain_at_the_middle.setFill ('red')
    mountain_at_the_middle.setOutline ('red')
    mountain_at_the_middle.draw(win)
    mountain_top.draw(win)
    mountain_top_2.draw(win)
                                        
                                        
    
    


def draw_birds(win):
    pass


def draw_sun(win):
    sun = gr.Circle(gr.Point(450, 180), 50)
    sun.setOutline('yellow')
    sun.setFill('yellow')
    sun.draw(win)


def draw_background(win):
    """Draws wall and floor"""
    sky_above = gr.Rectangle(gr.Point(0, 0), gr.Point(900, 180))
    sky_above.setOutline('burlywood1')
    sky_above.setFill('burlywood1')
    sky_beneath = gr.Rectangle(gr.Point(0, 180), gr.Point(900, 360))
    sky_beneath.setFill('pink')
    sky_beneath.setOutline('pink')
    sand = gr.Rectangle(gr.Point(0, 360), gr.Point(900, 540))
    sand.setFill ('LightGoldenrod1')
    sand.setOutline('LightGoldenrod1')
    abyss= gr.Rectangle(gr.Point(0, 540), gr.Point(900, 900))
    abyss.setFill ('thistle')
    abyss.setOutline('thistle')
    sky_above.draw(win)
    sky_beneath.draw(win)
    sand.draw(win)
    abyss.draw(win)
    

    
def main(win):
    """Draw picture"""
    draw_background(win)
    draw_sun(win)
    draw_mountain_at_the_middle(win)
    draw_mountain_above(win)
    draw_mountain_at_the_middle(win)

    
w = gr.GraphWin('pic8_1', 900, 900)

main(w)
w.getMouse()
w.close()
