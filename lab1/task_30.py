#!/usr/bin/python3

from pyrob.api import *





 
 
@task(delay=0.1)
def task_9_3():
    i=1
    b=0
    k=1
    while not wall_is_beneath():
        move_down()
        i+=1
    while not wall_is_above():
        move_up()
    while True:
    
        for  k in range (i-1):
            move_down()
            if b<i-2:
                fill_cell()
                b+=1
        b=0
        for k in range (i-1):
            move_right()
            if b<i-2:
                fill_cell()
                b+=1
        b=0
        for k in range(i-1):
            move_up()
            if b<i-2:
                fill_cell()
                b+=1
        b=0
        for k in range (i-1):
            move_left()
            if b<i-2:
                fill_cell()
                b+=1
        b=0
        
        i-=2
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
