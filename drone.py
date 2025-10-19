import carrot
import grass
import sunflower
import tree
import utils
from __builtins__ import *


def func():
    for _ in range(get_world_size()):
        if can_harvest():
            harvest()
        move(North)


def main():
    plant_list = [
        grass.line,
        tree.line,
        carrot.line,
        sunflower.line,
    ]

    utils.move_origin()

    while True:
        if len(plant_list) > 1:
            index = get_pos_x() % len(plant_list)
        else:
            index = 0
        func = plant_list[index]

        if num_drones() < max_drones():
            if not spawn_drone(func):
                func()
        else:
            func()
        move(East)


if __name__ == '__main__':
    main()
