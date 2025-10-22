import utils
from __builtins__ import *


# 单格
def one():
    if can_harvest():
        harvest()
    if get_ground_type() != Grounds.Soil:
        till()
    plant(Entities.Sunflower)
    utils.water()


# 一列
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
        utils.move_origin()


if __name__ == '__main__':
    main()
