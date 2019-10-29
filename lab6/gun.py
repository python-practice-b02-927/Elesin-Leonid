from random import randrange as rnd, choice
from tkinter import mainloop
import tkinter as tk
import math
import time


root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x600')
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)


class ball():
    """Creating bullets for gun"""
    def __init__(self, x=40, y=450):
        self.x = x
        self.y = y
        self.r = 5
        self.vx = 0
        self.vy = 0
        self.color = choice(['blue', 'green', 'red', 'yellow'])
        self.id = canv.create_oval(
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r,
                fill=self.color
        )
        self.live = 60

    def set_coords(self):
        canv.coords(
                self.id,
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r
        )

    def move(self):
        self.x += self.vx
        self.y -= self.vy
        self.vy += -1.5
        self.vx = 0.96*self.vx
        self.vy = 0.96*self.vy
        if self.x > (790-self.r):
            self.vx = -self.vx
        if self.y > (590-self.r):
            self.vy = -self.vy
        if self.x < self.r:
            self.vx = -self.vx
        if self.y < self.r:
            self.vy = -self.vy
        self.set_coords()

    def hittest(self, obj):
        if abs(obj.x-self.x) <= (self.r+obj.r) and abs(obj.y-self.y) <= (self.r+obj.r):
            return True
        else:
            return False


class gun():
    """Creating gun"""
    def __init__(self):
        self.f2_power = 5
        self.f2_on = 0
        self.an = 1
        self.id = canv.create_line(20, 450, 50, 420, width=7)

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        global balls, bullet
        bullet += 1
        new_ball = ball()
        new_ball.r += 5
        self.an = math.atan((event.y-new_ball.y) / (event.x-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 5

    def targetting(self, event=0):
        if event:
            self.an = math.atan((event.y-450) / (event.x-20))
        if self.f2_on:
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')
        canv.coords(self.id, 20, 450,
                    20 + max(self.f2_power, 20) * math.cos(self.an),
                    450 + max(self.f2_power, 20) * math.sin(self.an)
                    )

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')


class target_ver():
    """Creating first type of targets"""
    def __init__(self):
        self.points = 0
        self.live = 1
        self.id = canv.create_oval(0, 0, 0, 0)
        self.new_target()

    def new_target(self):
        x = self.x = rnd(600, 700)
        y = self.y = rnd(300, 500)
        r = self.r = rnd(10, 30)
        self.uy = rnd(-10, 10)
        color = self.color = 'red'
        canv.coords(self.id, x-r, y-r, x+r, y+r)
        canv.itemconfig(self.id, fill=color)

    def move(self):
        self.y += self.uy
        canv.coords(self.id, self.x - self.r,
                    self.y - self.r, self.x + self.r, self.y + self.r)
        if self.y > (600-self.r):
            self.uy = -self.uy
        if self.y < (self.r):
            self.uy = -self.uy


class target_hor():
    """Creating second type of targets"""
    def __init__(self):
        self.points = 0
        self.live = 1
        self.id = canv.create_oval(0, 0, 0, 0)
        self.new_target()

    def new_target(self):
        x = self.x = rnd(200, 600)
        y = self.y = rnd(100, 200)
        r = self.r = rnd(10, 30)
        self.ux = rnd(-10, 10)
        color = self.color = 'red'
        canv.coords(self.id, x-r, y-r, x+r, y+r)
        canv.itemconfig(self.id, fill=color)

    def move(self):
        self.x += self.ux
        canv.coords(self.id, self.x - self.r,
                    self.y - self.r, self.x + self.r, self.y + self.r)
        if self.x > (800-self.r):
            self.ux = -self.ux
        if self.x < (self.r):
            self.ux = -self.ux


t1 = target_ver()
t2 = target_hor()
g1 = gun()
scores = 0
screen1 = canv.create_text(400, 300, text='', font='28')
screen2 = canv.create_text(30, 30, text='', font='28')


def new_game(event=''):
    global gun, t1, screen1, screen2, balls, bullet, scores
    t1.new_target()
    t2.new_target()
    bullet = 0
    balls = []
    canv.bind('<Button-1>', g1.fire2_start)
    canv.bind('<ButtonRelease-1>', g1.fire2_end)
    canv.bind('<Motion>', g1.targetting)
    t1.live = 1
    t2.live = 1
    while t1.live or t2.live:
        for b in (balls):
            b.move()
            if b.hittest(t1):
                t1.live = 0
                canv.coords(t1.id, 0, 0, 0, 0)
            if b.hittest(t2):
                t2.live = 0
                canv.coords(t2.id, 0, 0, 0, 0)
            b.live -= 1
            if b.live < 0:
                canv.delete(b.id)
        if t1.live == 1:
            t1.move()
        if t2.live == 1:
            t2.move()
        canv.update()
        time.sleep(0.03)
        g1.targetting()
        g1.power_up()
    scores += 1
    canv.itemconfig(screen1,
                    text='Вы уничтожили цели c ' + str(bullet) + ' попытки')
    canv.itemconfig(screen2, text=str(scores))
    for b in balls:
        canv.delete(b.id)
    canv.update()
    time.sleep(0.7)
    canv.itemconfig(screen1, text='')
    root.after(0,  new_game)

new_game()
mainloop()
