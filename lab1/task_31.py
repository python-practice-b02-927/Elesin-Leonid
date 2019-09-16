#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.001)
def task_8_30():
        i=0
        while 1:
                while not wall_is_on_the_right():
                        move_right()
                i+=1
                while not wall_is_on_the_left():
                        move_left()
                        if not wall_is_beneath():
                            move_down()
                            i=0
                if i==1:
                    break
                
                            
                



if __name__ == '__main__':
    run_tasks()
