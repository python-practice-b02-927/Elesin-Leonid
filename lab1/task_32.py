#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_8_18():
    i=0 
    while wall_is_beneath():
        if wall_is_above() and wall_is_beneath():
            fill_cell()
        
        
            
        if not wall_is_above():
            while not wall_is_above():
                move_up()
                if not cell_is_filled():
                    fill_cell()
                else:
                    i=i+1
 
            while not wall_is_beneath():
                move_down()
        move_right()
            
        
    mov('ax', i)
    



if __name__ == '__main__':
    run_tasks()
