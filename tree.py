import utils
from __builtins__ import *


# 单格
def one():
    if can_harvest():
        harvest()
    if get_ground_type() != Grounds.Grassland:
        till()
    # 棋盘布局种植树木和干草
    if (get_pos_x() + get_pos_y()) % 2 == 0:
        plant(Entities.Tree)
        utils.water()


# 单列
def column():
    utils.move_to(get_pos_x(), 0)
    for _ in range(get_world_size()):
        one()
        utils.scan_column()


# 整场
def main():
    utils.move_origin()
    while True:
        utils.multiple(column)


if __name__ == '__main__':
    main()
