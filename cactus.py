import utils
from __builtins__ import *


# 种植单格
def plant_one():
    if get_ground_type() != Grounds.Soil:
        till()
    if get_entity_type() == None:
        if num_items(Items.Cactus) > 0:
            plant(Entities.Cactus)
    # utils.water()


# 种植单列
def plant_column():
    for _ in range(get_world_size()):
        plant_one()
        utils.scan_column()


# 排序单列
def sort_column():
    utils.move_to(get_pos_x(), 0)
    for j in range(get_world_size()):
        # 每次移到首位
        utils.move_to(get_pos_x(), 0)
        # 如果没发生交换，说明已排好序，可以直接跳过循环
        finished = True
        # 一直移动，直到已排好的前面停下
        while get_pos_y() < get_world_size() - 1 - j:
            # 前面比后面大就交换
            current_num = measure()
            next_num = measure(North)
            if current_num > next_num:
                finished = False
                swap(North)
            utils.scan_column()
        if finished:
            break


# 排序单行
def sort_row():
    utils.move_to(0, get_pos_y())
    for j in range(get_world_size()):
        # 每次移到首位
        utils.move_to(0, get_pos_y())
        # 如果没发生交换，说明已排好序，可以直接跳过循环
        finished = True
        # 一直移动，直到已排好的前面停下
        while get_pos_x() < get_world_size() - 1 - j:
            # 前面比后面大就交换
            current_num = measure()
            next_num = measure(East)
            if current_num > next_num:
                finished = False
                swap(East)
            utils.scan_row()
        if finished:
            break


def main():
    # set_execution_speed(6)
    utils.clear_gently(True)
    # 种植——排序——收获
    while True:
        # 种植整场
        change_hat(Hats.Purple_Hat)
        utils.multiple_column(plant_column)

        # 先对列做冒泡排序
        change_hat(Hats.Green_Hat)
        utils.multiple_column(sort_column)

        # 再对行做冒泡排序
        # 等列排序全部结束后再执行行排序
        while num_drones() > 1:
            pass
        change_hat(Hats.Brown_Hat)
        utils.multiple_row(sort_row)

        # 排序完成，一键收获
        # 等行排序全部结束后再执行收获
        while num_drones() > 1:
            pass
        change_hat(Hats.Gray_Hat)
        if can_harvest():
            harvest()
        utils.move_origin()


if __name__ == '__main__':
    main()
