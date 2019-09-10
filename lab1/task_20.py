#!/usr/bin/python3

from pyrob.api import *

def stroka():
    x=0
    
    while x<27:
        move_right()
        fill_cell()
        x=x+1
    move_down()
    fill_cell()
    x=0
    while x<26:
        move_left()
        fill_cell()
        x=x+1
    move_left()
    move_down()


@task(delay=0.05)
def task_4_3():
    b=0
    while b<6:
       stroka()
       b=b+1
    move_right()
 
    
 


if __name__ == '__main__':
    run_tasks()
