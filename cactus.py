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
            # 一直移动，直到已排好的前面停下
            while get_pos_y() < get_world_size() - 1 - j:
                # 前面比后面大就交换
                current_num = measure()
                next_num = measure(North)
                if current_num > next_num:
                    swap(North)
                move(North)
        move(East)

    utils.move_origin()

    for i in range(get_world_size()):
        for j in range(get_world_size()):
            # 每次移到首位
            utils.move_to(0, get_pos_y())
            # 一直移动，直到已排好的前面停下
            while get_pos_x() < get_world_size() - 1 - j:
                # 前面比后面大就交换
                current_num = measure()
                next_num = measure(East)
                if current_num > next_num:
                    swap(East)
                move(East)
        move(North)


def main():
    # 清空农场
    utils.clear_gently()
    clear()
    # 种植——先列后行，冒泡排序——收获
    while True:
        plant_all()
        sort_all()
        if can_harvest():
            harvest()


if __name__ == '__main__':
    main()
