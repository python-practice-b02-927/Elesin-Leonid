import graphics as gr


def draw_body_and_tail(win):
    pass


def draw_head(win):
    pass


def draw_legs(win):
    pass


def draw_window(win):
    pass


def draw_background(win):
    """Draws wall and floor"""
    wall = gr.Rectangle(gr.Point(0, 0), gr.Point(600, 400))
    wall.setFill('orange4')
    floor = gr.Rectangle(gr.Point(0, 400), gr.Point(600, 900))
    floor.setFill('goldenrod4')
    wall.draw(win)
    floor.draw(win)

    
def main(win):
    """Draw picture"""
    draw_background(win)

    
w = gr.GraphWin('pic8_1', 600, 900)

main(w)
w.getMouse()
w.close()
