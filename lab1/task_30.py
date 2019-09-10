#!/usr/bin/python3

from pyrob.api import *





 
 
@task(delay=0.1)
def task_9_3():
    i=1
    b=0
    k=1
    while not wall_is_beneath():
        move_down()
        i=i+1
    while not wall_is_above():
        move_up()
    while True:
    
        while k<i:
            move_down()
            k=k+1
            if b<i-2:
                fill_cell()
                b=b+1
        b=0
        k=1
        while k<i:
            move_right()
            k=k+1
            if b<i-2:
                fill_cell()
                b=b+1
        b=0
        k=1
        while k<i:
            move_up()
            k=k+1
            if b<i-2:
                fill_cell()
                b=b+1
        b=0
        k=1
        while k<i:
            move_left()
            k=k+1
            if b<i-2:
                fill_cell()
                b=b+1
        b=0
        k=1
        
        i=i-2
        if i==1:
            break
        move_down()
        move_right()
    while not wall_is_on_the_left():
        move_left()
    while not wall_is_beneath():
        move_down()
        
        
    


if __name__ == '__main__':
    run_tasks()



if __name__ == '__main__':
    run_tasks()
