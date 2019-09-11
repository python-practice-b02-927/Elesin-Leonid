#!/usr/bin/python3

from pyrob.api import *


def fill_lower():
	move_down()
	fill_cell()
	move_up()

def fill_upper():
	move_up()
	fill_cell()
	move_down()





def fill_upper_and_lower_cells():
	if not wall_is_above() and wall_is_beneath():
		fill_upper()
	if not wall_is_beneath() and wall_is_above():
		fill_lower()
	if not wall_is_beneath() and not wall_is_above():
		fill_upper()
		fill_lower()
	if wall_is_beneath() and wall_is_above():
		fill_cell()


@task
def task_8_11():
	while True:
		fill_upper_and_lower_cells()
		if wall_is_on_the_right():
			break
		move_right()

if __name__ == '__main__':
    run_tasks()
