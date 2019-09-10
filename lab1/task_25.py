#!/usr/bin/python3

from pyrob.api import *

def kraska():
    fill_cell()
    move_down()
    move_right()
    fill_cell()
    move_up()
    fill_cell()
    move_up()
    fill_cell()
    move_right()
    move_down()
    fill_cell()

@task
def task_2_2():
    move_down(n=2)
    kraska()
    i=0
    while i<4:
        move_right(n=2)
        kraska()
        i=i+1
    move_up()
    move_left(n=2)

if __name__ == '__main__':
    run_tasks()
