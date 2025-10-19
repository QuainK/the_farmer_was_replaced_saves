import utils
from __builtins__ import *


# 一列
def line():
    for j in range(get_world_size()):
        if can_harvest():
            harvest()
        if get_ground_type() != Grounds.Soil:
            till()
        plant(Entities.Carrot)
        # utils.water()
        utils.scan_line()


def main():
    utils.move_origin()
    while True:
        for i in range(get_world_size()):
            line()
            move(East)


if __name__ == '__main__':
    main()
