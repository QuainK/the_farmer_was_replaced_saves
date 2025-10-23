import utils
from __builtins__ import *


# 区域种植
def area_plant():
    origin_x = get_pos_x()
    for i in range(6):
        x = get_pos_x()
        for j in range(6):
            if can_harvest():
                harvest()
            if get_ground_type() != Grounds.Soil:
                till()
            if num_items(Items.Pumpkin) > 0:
                plant(Entities.Pumpkin)
            # Z字形扫描
            # 要注意相对区域原点的偏移量
            if (x - origin_x) % 2 == 0:
                if j < 5:
                    move(North)
            else:
                if j < 5:
                    move(South)
        if i < 5:
            move(East)


# 区域扫描坏南瓜记录到列表里
def area_scan_bad():
    origin_x = get_pos_x()
    # 坏南瓜坐标列表
    bad_list = []
    for i in range(6):
        x = get_pos_x()
        for j in range(6):
            if get_entity_type() == Entities.Dead_Pumpkin:
                bad_list.append([get_pos_x(), get_pos_y()])
                if num_items(Items.Carrot) > 0:
                    plant(Entities.Pumpkin)
            # utils.water()
            # Z字形扫描
            # 要注意相对区域原点的偏移量
            if (x - origin_x) % 2 == 0:
                if j < 5:
                    move(North)
            else:
                if j < 5:
                    move(South)
        if i < 5:
            move(East)
    return bad_list


# 区域处理坏南瓜，重新种植，如果坏南瓜在下次检测时是好的，那就在列表里标记
def area_handle_bad(bad_list):
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
            # utils.water()
        # 翻滚动作是为了等待下一波遍历，或者是等最后一个坏南瓜成熟
        do_a_flip()
        if all_ok:
            break


# 区域运行
def area():
    while True:
        # 种植
        origin_x = get_pos_x()
        origin_y = get_pos_y()
        area_plant()
        # 检测
        utils.move_to(origin_x, origin_y)
        bad_list = area_scan_bad()
        # 处理
        utils.move_to(origin_x, origin_y)
        area_handle_bad(bad_list)
        # 收获，清空列表，回到原点，开始新的一轮种植
        if can_harvest():
            harvest()
            bad_list = []
        utils.move_to(origin_x, origin_y)


def main():
    utils.clear_gently(True)
    # set_execution_speed(4)
    # 将农场划分成多个区域，每个区域是6*6，这样可以尽可能获得更多的南瓜
    # 分区——种植——检测——处理

    # 划分区域
    # 每个6*6之间都可以用一行或一列做为隔离
    # 每块区域的原点，也就是左下角，坐标满足一定的模运算（取余数），比如
    # [0,28]         ...       [28,28]
    # [0,21]         ...          .
    # [0,14]         ...          .
    # [0,7]          ...          .
    # [0,0] [7,0] [14,0] [21,0] [28,0]
    # 看起来横纵坐标都是7的n倍
    change_hat(Hats.Purple_Hat)
    # 派出子无人机到各个区域的原点
    for i in range(get_world_size()):
        # 确定列
        x = get_pos_x()
        # 剩余区域不够了，跳过
        if get_world_size() - x < 6:
            break
        if x % 7 == 0:
            # print(x)
            for j in range(get_world_size()):
                # 确定行
                y = get_pos_y()
                # 剩余区域不够了，跳过
                if get_world_size() - y < 6:
                    break
                # 如果当前坐标能派出子无人机就派出，不能就跳过
                if y % 7 == 0:
                    if num_drones() < max_drones():
                        spawn_drone(area)
                    else:
                        area()
                utils.scan_column()
            utils.move_to(x, 0)
        utils.scan_row()


if __name__ == '__main__':
    main()
