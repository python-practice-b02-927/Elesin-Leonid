import graphics as gr


def draw_(win):
    """draw body and tail"""
    


def draw_mountains(win):
    pass


def draw_birds(win):
    pass


def draw_sun(win):
    pass


def draw_background(win):
    """Draws wall and floor"""
    sky_above = gr.Rectangle(gr.Point(0, 0), gr.Point(900, 180))
    sky_above.setFill('burlywood1')
    sky_beneath = gr.Rectangle(gr.Point(0, 180), gr.Point(900, 360))
    sky_beneath.setFill('pink')
    sand = gr.Rectangle(gr.Point(0, 360), gr.Point(900, 540))
    sand.setFill ('LightGoldenrod1')
    abyss= gr.Rectangle(gr.Point(0, 540), gr.Point(900, 900))
    abyss.setFill ('thistle')
    sky_above.draw(win)
    sky_beneath.draw(win)
    sand.draw(win)
    abyss.draw(win)
    

    
def main(win):
    """Draw picture"""
    draw_background(win)

    
w = gr.GraphWin('pic8_1', 900, 900)

main(w)
w.getMouse()
w.close()
