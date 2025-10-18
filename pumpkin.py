import utils
from __builtins__ import *

# 坏南瓜坐标列表
bad_list = []


# 种植整个农场
def plant_all():
    global bad_list
    for i in range(get_world_size()):
        for j in range(get_world_size()):
            if get_ground_type() != Grounds.Soil:
                till()
            if get_entity_type() == None:
                if num_items(Items.Carrot) > 0:
                    plant(Entities.Pumpkin)
            utils.water()
            # Z字形扫描
            if j >= get_world_size() - 1:
                break
            if i % 2 == 0:
                move(North)
            else:
                move(South)
        move(East)


# 扫描坏南瓜记录到列表里
def scan_bad():
    global bad_list
    for i in range(get_world_size()):
        for j in range(get_world_size()):
            if get_entity_type() == Entities.Dead_Pumpkin:
                bad_list.append([get_pos_x(), get_pos_y()])
                if num_items(Items.Carrot) > 0:
                    plant(Entities.Pumpkin)
            utils.water()
            # Z字形扫描
            if j >= get_world_size() - 1:
                break
            if i % 2 == 0:
                move(North)
            else:
                move(South)
        move(East)


# 处理坏南瓜，重新种植，如果坏南瓜在下次检测时是好的，那就从列表里移除
def handle_bad():
    global bad_list
    # 遍历坏南瓜列表
    while len(bad_list) > 0:
        # 假设南瓜都是好的，一旦有坏南瓜，变成False
        all_ok = True
        for index in range(len(bad_list)):
            # 取出第一个坏南瓜的坐标
            location = bad_list[index]
            if location == None:
                continue
            # 飞过去
            utils.move_to(location[0], location[1])
            # 如果还是坏南瓜，就重新种植
            if get_entity_type() == Entities.Dead_Pumpkin or can_harvest() == False:
                all_ok = False
                if num_items(Items.Carrot) > 0:
                    plant(Entities.Pumpkin)
            # 如果转成好南瓜了，就将这个坐标清空
            # 为什么不支持移除，因为正在遍历列表时，修改列表长度会导致意外情况
            # 这里用一个None标记，代表当前坐标已经是好南瓜了，可以跳过，这样更加稳健
            else:
                bad_list[index] = None
            utils.water()
        # 翻滚动作是为了等待下一波遍历，或者是等最后一个坏南瓜成熟
        do_a_flip()
        if all_ok:
            break

    # 收获，清空列表，回到原点，开始新的一轮种植
    if can_harvest():
        harvest()
        bad_list = []
    utils.move_origin()


def main():
    global bad_list
    bad_list = []
    # 清空农场
    utils.clear_gently()
    clear()
    # 种植——检测——处理
    while True:
        change_hat(Hats.Purple_Hat)
        plant_all()

        change_hat(Hats.Green_Hat)
        scan_bad()

        change_hat(Hats.Brown_Hat)
        handle_bad()


if __name__ == '__main__':
    main()
