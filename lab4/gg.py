from tkinter import *
from random import randrange as rnd, choice
import time
root = Tk()
root.geometry('900x900')

"""Creating label"""
l = Label(root, bg='black', fg='white', width=20)
l.pack()


"""Creating canvas"""
canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)

"""Add colors to figures"""
colors = ['red', 'orange', 'yellow', 'green', 'blue']

scores = 0
balls = {}
sqares = {}


"""Functions to delete figures"""


def del_ball(ball):
    del balls[ball['id']]
    canv.delete(ball['id'])


def del_sqares(sqare):
    del sqares[sqare['id']]
    canv.delete(sqare['id'])


"""Functions to create new balls"""


def new_ball():
    b = {'x': rnd(100, 700), 'y': rnd(100, 500), 'r': rnd(30, 50)}
    b['id'] = canv.create_oval(b['x']-b['r'], b['y']-b['r'], b['x']+b['r'],
                               b['y']+b['r'], fill=choice(colors), width=0)
    balls[b['id']] = b

    root.after(5000, del_ball, b)
    root.after(1000, new_ball)


def new_sqares():
    s = {'x': rnd(100, 700), 'y': rnd(100, 500), 'r': rnd(60, 100)}
    s['id'] = canv.create_rectangle(s['x'], s['y'], s['x']+s['r'],
                                    s['y']+s['r'], fill=choice(colors),
                                    width=0)
    sqares[s['id']] = s

    root.after(1000, del_sqares, s)
    root.after(250, new_sqares)


"""Function to click"""


def click(event):
    global scores
    for id_ in balls:
        if ((balls[id_]['x'] - event.x)**2 + (balls[id_]['y'] -
           event.y)**2)**0.5 < balls[id_]['r']:
            scores += 1
            del_ball(balls[id_])
            l['text'] = scores
    for id_ in sqares:
        if ((sqares[id_]['x'] + sqares[id_]['r']*0.5 - event.x)**2 +
           (sqares[id_]['y'] + sqares[id_]['r']*0.5 -
           event.y)**2)**0.5 < sqares[id_]['r']*0.5:
            scores += 3
            del_sqares(sqares[id_])
            l['text'] = scores


new_ball()
new_sqares()
canv.bind('<Button-1>', click)
mainloop()

