import graphics as gr


w = gr.GraphWin('pic5_2', 900, 900)


def draw_mountain_above(win):
    """Draws mountain on the top"""
    mountain_above = gr.Polygon(gr.Point(20, 390), gr.Point(900, 270),
                                gr.Point(795, 225), gr.Point(750, 250),
                                gr.Point(700, 210 ),gr.Point(650, 220),
                                gr.Point(580,140),gr.Point(570,143),
                                gr.Point(545,180),gr.Point(490,257),
                                gr.Point(454,258),gr.Point(424,283),
                                gr.Point(388,266),gr.Point(352,343),
                                gr.Point(316,312),gr.Point(256,344),
                                gr.Point(149,200),gr.Point(136,180),
                                gr.Point(117,170),gr.Point(98,313),
                                gr.Point(88,328),gr.Point(42,345))
    mountain_above.setFill (gr.color_rgb(252,152,49))
    mountain_above.setOutline (gr.color_rgb(252,152,49))
    mountain_above.draw(win)


def draw_mountain_at_the_middle(win):
    """Draws mountain at the middle"""
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
    mountain_top = gr.Oval(gr.Point(50, 350), gr.Point(140, 540))
    mountain_top.setFill (gr.color_rgb(172,67,52))
    mountain_top.setOutline(gr.color_rgb(172,67,52))
    mountain_top_2=gr.Oval (gr.Point(439,357), gr.Point(525,495))
    mountain_top_2.setFill(gr.color_rgb(172,67,52))
    mountain_top_2.setOutline(gr.color_rgb(172,67,52))
    mountain_at_the_middle.setFill (gr.color_rgb(172,67,52))
    mountain_at_the_middle.setOutline (gr.color_rgb(172,67,52))
    mountain_at_the_middle.draw(win)
    mountain_top.draw(win)
    mountain_top_2.draw(win)


def draw_mountain_beneath(win):
    """Draws mountain on the bottom"""
    mountain_beneath = gr.Polygon(gr.Point(0,402), gr.Point(84,432),
                                  gr.Point(170,579), gr.Point(278,837),
                                  gr.Point(338,863), gr.Point(464,871),
                                  gr.Point(599,712), gr.Point(664,737),
                                  gr.Point(720,769), gr.Point(764,777),
                                  gr.Point(792,767), gr.Point(828,645),
                                  gr.Point(857,584), gr.Point(900,518),
                                  gr.Point(900,900), gr.Point(0,900))
    mountain_beneath.setFill (gr.color_rgb(48,16,38))
    mountain_beneath.setOutline (gr.color_rgb(48,16,38))
    mountain_beneath.draw(win)
                                    
                                           
def draw_birds(win):
    """Draws birds"""
    bird1 = gr.Polygon(gr.Point(348,326),gr.Point(322,305),
                     gr.Point(347,315),gr.Point(374,305))
    bird2 = gr.Polygon(gr.Point(426,338),gr.Point(404,315),
                     gr.Point(430,328),gr.Point(457,314))
    bird3 = gr.Polygon(gr.Point(426,382),gr.Point(402,360),
                     gr.Point(428,372),gr.Point(455,360))
    bird4 = gr.Polygon(gr.Point(358,421),gr.Point(334,398),
                     gr.Point(360,411),gr.Point(385,397))
    bird5 = gr.Polygon(gr.Point(564,611),gr.Point(539,585),
                     gr.Point(567,601),gr.Point(595,588))
    bird6 = gr.Polygon(gr.Point(614,676),gr.Point(590,656),
                     gr.Point(614,666),gr.Point(641,654))
    bird7 = gr.Polygon(gr.Point(716,652),gr.Point(696,633),
                     gr.Point(715,641),gr.Point(743,632))
    bird8 = gr.Polygon(gr.Point(701,722),gr.Point(664,688),
                     gr.Point(701,704),gr.Point(740,686))
    bird1.setFill(gr.color_rgb(66, 33, 11))
    bird1.setOutline(gr.color_rgb(66, 33, 11))
    bird2.setFill(gr.color_rgb(66, 33, 11))
    bird2.setOutline(gr.color_rgb(66, 33, 11))
    bird3.setFill(gr.color_rgb(66, 33, 11))
    bird3.setOutline(gr.color_rgb(66, 33, 11))
    bird4.setFill(gr.color_rgb(66, 33, 11))
    bird4.setOutline(gr.color_rgb(66, 33, 11))
    bird5.setFill(gr.color_rgb(66, 33, 11))
    bird5.setOutline(gr.color_rgb(66, 33, 11))
    bird6.setFill(gr.color_rgb(66, 33, 11))
    bird6.setOutline(gr.color_rgb(66, 33, 11))
    bird7.setFill(gr.color_rgb(66, 33, 11))
    bird7.setOutline(gr.color_rgb(66, 33, 11))
    bird8.setFill(gr.color_rgb(66, 33, 11))
    bird8.setOutline(gr.color_rgb(66, 33, 11))
    bird1.draw(win)
    bird2.draw(win)
    bird3.draw(win)
    bird4.draw(win)
    bird5.draw(win)
    bird6.draw(win)
    bird7.draw(win)
    bird8.draw(win)


def draw_sun(win):
    """Draws sun"""
    sun = gr.Circle(gr.Point(450, 180), 50)
    sun.setOutline(gr.color_rgb(252,238,33))
    sun.setFill(gr.color_rgb(252,238,33))
    sun.draw(win)


def draw_background(win):
    """Draws sky, sand and abyss"""
    sky_above = gr.Rectangle(gr.Point(0, 0), gr.Point(900, 180))
    sky_above.setOutline(gr.color_rgb(254,213,162))
    sky_above.setFill(gr.color_rgb(254,213,162))
    sky_beneath = gr.Rectangle(gr.Point(0, 180), gr.Point(900, 360))
    sky_beneath.setFill(gr.color_rgb(254,213,196))
    sky_beneath.setOutline(gr.color_rgb(254,213,196))
    sand = gr.Rectangle(gr.Point(0, 360), gr.Point(900, 540))
    sand.setFill (gr.color_rgb(254,213,148))
    sand.setOutline(gr.color_rgb(254,213,148))
    abyss= gr.Rectangle(gr.Point(0, 540), gr.Point(900, 900))
    abyss.setFill (gr.color_rgb(179,134,148))
    abyss.setOutline(gr.color_rgb(179,134,148))
    sky_above.draw(win)
    sky_beneath.draw(win)
    sand.draw(win)
    abyss.draw(win)
    
    
def main(win):
    """Draws picture"""
    draw_background(win)
    draw_sun(win)
    draw_mountain_at_the_middle(win)
    draw_mountain_above(win)
    draw_mountain_at_the_middle(win)
    draw_mountain_beneath(win)
    draw_birds(win)


main(w)
w.getMouse()
w.close()
