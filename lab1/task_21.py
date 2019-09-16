#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_4_11():

    for z in range(13):
        
        for i in range (13-z):
            move_down()
            move_right()
            fill_cell()
        
        for b in range (12-z):
            move_left()
            move_up()
            
        move_left()
        z+=1
    move_down()
    move_right()
        
    


if __name__ == '__main__':
    run_tasks()
