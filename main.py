import carrot
import grass
import sunflower
import tree
import utils
from __builtins__ import *


# 按列种植不同作物
def plant_by_line():
    plant_list = [
        grass.line,
        tree.line,
        carrot.line,
        sunflower.line,
    ]

    for i in range(get_world_size()):
        if i >= len(plant_list):
            break
        plant_list[i % len(plant_list)]()
        move(East)


# 种植基础作物，干草，木头，能量
def plant_basic_items():
    for i in range(get_world_size()):
        if num_items(Items.Power) <= 1000:
            sunflower.line()
        else:
            tree.line()
        move(East)


def main():
    # 清空农场
    utils.clear_gently()

    # 种植和收获
    while True:
        # plant_by_line()
        plant_basic_items()


if __name__ == '__main__':
    main()
