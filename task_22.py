#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_10():
    fill_cell()
    b=1
    k=0
    while not wall_is_on_the_right():
        move_right()
        fill_cell()
    while not wall_is_on_the_left():
        move_left()
    
    while not wall_is_beneath():
    
        move_down()
        fill_cell()
        while not wall_is_on_the_right():
            move_right()
            fill_cell()
        while not wall_is_on_the_left():
            move_left()
        if wall_is_beneath():
            break
       
        
        


if __name__ == '__main__':
    run_tasks()
