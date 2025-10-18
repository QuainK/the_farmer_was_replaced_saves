import utils
from __builtins__ import *


def main():
    # 清空农场
    utils.clear_gently()

    # 种植和收获
    while True:
        for i in range(get_world_size()):
            for j in range(get_world_size()):
                if can_harvest():
                    harvest()
                if i == 2 or i == 3:
                    if (i + j) % 2 == 0:
                        plant(Entities.Tree)
                elif i == 4 or i == 5:
                    if get_ground_type() != Grounds.Soil:
                        till()
                    plant(Entities.Carrot)
                move(North)
            move(East)


if __name__ == '__main__':
    main()
