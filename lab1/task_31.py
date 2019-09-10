#!/usr/bin/python3

from pyrob.api import *

    


@task(delay=0.05)
def task_8_30():
    i=0
    b=0
    while True:
        while not wall_is_on_the_left():
            move_left() 
            if not wall_is_beneath():
                i=i+1
        b=b+1
            
        while not wall_is_on_the_right():
            move_right()
            if not wall_is_beneath():
                i=i+1
        b=b+1
        if i>0:
            while wall_is_beneath():
                move_left()
            while not wall_is_beneath():
                move_down()
            b=0
            i=0
        if b==2:
            break
        i=0
    while not wall_is_on_the_left():
        move_left()
        

if __name__ == '__main__':
    run_tasks()
