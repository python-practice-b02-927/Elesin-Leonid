#!/usr/bin/python3

from pyrob.api import *

def krest():
    
    fill_cell()
    move_down()
    move_right()
    fill_cell()
    move_up()
    fill_cell()
    move_up()
    fill_cell()
    move_right()
    move_down()
    fill_cell()
def polosa():
    i=0
    move_down()
    krest()
    while i<9:
        move_right(n=2)
        krest()
        i=i+1
    while not wall_is_on_the_left():
        move_left()
    move_up()

@task(delay=0.02)
def task_2_4():
    k=0
    polosa()
    while k<4:
        move_down(n=4)
        polosa()
        k=k+1
    


if __name__ == '__main__':
    run_tasks()
