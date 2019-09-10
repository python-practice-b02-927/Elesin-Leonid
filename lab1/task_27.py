#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_5():
    b=-1
    i=0
    while not wall_is_on_the_right():
        move_right()
        b=b+1
        if i==b:
            fill_cell()
            b=0
            i=i+1
        
    
        


if __name__ == '__main__':
    run_tasks()
