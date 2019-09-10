#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_4_11():
    i=0
    b=0
    z=0
    while z<=12:
        
        while i<13-z:
            move_down()
            move_right()
            fill_cell()
            i=i+1
        while b<12-z:
            move_left()
            move_up()
            b=b+1
        move_left()
        i=0
        b=0
        z=z+1
    move_down()
    move_right()
        
    


if __name__ == '__main__':
    run_tasks()
