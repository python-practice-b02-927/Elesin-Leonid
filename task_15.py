#!/usr/bin/python3

from pyrob.api import *


def walk_hor():
	if not wall_is_on_the_right():
		while not wall_is_on_the_right():
			move_right()
	elif not wall_is_on_the_left():
		while not wall_is_on_the_left():
			move_left()



def walk_ver():
	if not wall_is_above():
		while not wall_is_above():
			move_up()
	elif not wall_is_beneath():
		while not wall_is_beneath():
			move_down()


@task
def task_8_21():
	walk_hor()
	walk_ver()


 


if __name__ == '__main__':
    run_tasks()
