#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_27():
    i=0
    while(i<=11):
        move_up()
        if cell_is_filled():
            move_left()
            if cell_is_filled():
                break
            else:
                move_right(n=2)
                break
        


if __name__ == '__main__':
    run_tasks()
