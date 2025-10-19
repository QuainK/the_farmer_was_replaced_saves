import utils
from __builtins__ import *


# 种植整个农场
def plant_all():
    for i in range(get_world_size()):
        for j in range(get_world_size()):
            if get_ground_type() != Grounds.Soil:
                till()
            if get_entity_type() == None:
                plant(Entities.Cactus)
            move(North)
        move(East)


# 冒泡排序真个农场，先列后行
def sort_all():
    for i in range(get_world_size()):
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
                move(North)
            if finished:
                break
        move(East)

    utils.move_origin()

    for i in range(get_world_size()):
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
                move(East)
            if finished:
                break
        move(North)


def main():
    clear()
    # 种植——先列后行，冒泡排序——收获
    while True:
        plant_all()
        sort_all()
        if can_harvest():
            harvest()
        utils.move_origin()


if __name__ == '__main__':
    main()
