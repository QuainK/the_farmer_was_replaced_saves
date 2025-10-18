import utils
from __builtins__ import *


# 一列
def line():
    for j in range(get_world_size()):
        i = get_pos_x()
        if can_harvest():
            harvest()
        if (i + j) % 2 == 0:
            if get_ground_type() != Grounds.Soil:
                till()
            plant(Entities.Tree)
            utils.water()
        else:
            if get_ground_type() != Grounds.Grassland:
                till()
        move(North)


def main():
    # 清空农场
    utils.clear_gently()
    while True:
        for i in range(get_world_size()):
            line()
            move(East)


if __name__ == '__main__':
    main()
