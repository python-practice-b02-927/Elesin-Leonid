#!/usr/bin/python3

from pyrob.api import *

    


@task(delay=0.05)
def task_8_30():
    i=0
    b=0
    while 1:
        while not wall_is_on_the_right():
            while not wall_is_beneath():
                move_down()
                i=0
            move_right()
        i=i+1
        while not wall_is_on_the_left():
            while not wall_is_beneath():
                move_down()
                i=0
            move_left()
        i=i+1
        if i>1:
            break


        

if __name__ == '__main__':
    run_tasks()
