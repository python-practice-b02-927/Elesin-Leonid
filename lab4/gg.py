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

"""Add colors to figures and set constants"""
colors = ['red', 'orange', 'yellow', 'green', 'blue']
scores = 0
i = 0
balls = []
sqares = []
name = input()


def del_ball(b):
    """Function to delere ball after time"""
    if b in balls:
        canv.delete(balls[0]['id'])
        balls.pop(0)


def del_sqare(s):
    """Function to delete sqare after time"""
    if s in sqares:
        canv.delete(sqares[0]['id'])
        sqares.pop(0)


def new_ball():
    """Functions to create new balls"""
    b = {'x': rnd(100, 700), 'y': rnd(100, 500), 'r': rnd(30, 50),
         'vx': rnd(-10, 10), 'vy': rnd(-10, 10)}
    b['id'] = canv.create_oval(b['x']-b['r'], b['y']-b['r'], b['x']+b['r'],
                               b['y']+b['r'], fill=choice(colors), width=0)
    balls.append(b)
    root.after(6000, del_ball, b)
    root.after(1000, new_ball)


def new_sqares():
    """Function to create new sqares"""
    s = {'x': rnd(50, 850), 'y': rnd(50, 850), 'r': rnd(50, 100)}
    s['id'] = canv.create_rectangle(s['x'], s['y'], s['x']+s['r'],
                                    s['y']+s['r'], fill=choice(colors),
                                    width=0)
    sqares.append(s)
    root.after(8000, del_sqare, s)
    root.after(2000, new_sqares)


def movement():
    """Function to move"""
    for b in balls:
        if (b['x'] < b['r']) or b['x'] > (900-b['r']):
            b['vx'] = -b['vx']
        if (b['y'] < b['r']) or b['y'] > (900-b['r']):
            b['vy'] = -b['vy']
        canv.move(b['id'], b['vx'], b['vy'])
        b['x'] += b['vx']
        b['y'] += b['vy']
    root.after(30, movement)


def click(event):
    """Function to click"""
    global scores
    for i, b in enumerate(balls):
        if ((b['x'] - event.x)**2 + (b['y'] -
           event.y)**2)**0.5 < b['r']:
            scores += 3
            canv.delete(b['id'])
            balls.pop(i)
            l['text'] = scores
    for i, s in enumerate(sqares):
        if (abs(s['x'] - event.x) < s['r'] and abs(s['y'] - event.y) < s['r']):
            scores += 1
            canv.delete(s['id'])
            sqares.pop(i)
            l['text'] = scores


new_ball()
new_sqares()
movement()
canv.bind('<Button-1>', click)
mainloop()
my_file = open('Results.txt', 'a')
my_file.write(name + ' ' + str(scores) + '\n')
my_file.close()
