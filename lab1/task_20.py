#!/usr/bin/python3

from pyrob.api import *

def stroka():
    x=0
    
    for x in range(27):
        move_right()
        fill_cell()

    move_down()
    fill_cell()
    x=0
    for x in range (26):
        move_left()
        fill_cell()

    move_left()
    move_down()


@task(delay=0.05)
def task_4_3():
    b=0
    for b in range(6):
       stroka()
    move_right()
 
    
 


if __name__ == '__main__':
    run_tasks()

