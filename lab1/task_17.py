#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_27():
    while True:
        move_up()
        if cell_is_filled():
            break
    move_left()
    if not cell_is_filled():
        move_right(n=2)
        
        


if __name__ == '__main__':
    run_tasks()
