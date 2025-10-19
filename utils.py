from __builtins__ import *


# 移动到指定坐标
def move_to(x=0, y=0):
    while x != get_pos_x() or y != get_pos_y():
        if x < get_pos_x():
            move(West)
        elif x > get_pos_x():
            move(East)
        elif y < get_pos_y():
            move(South)
        elif y > get_pos_y():
            move(North)


# 移动到原点
def move_origin():
    move_to(0, 0)


# Z字形扫描
def z_scan():
    if get_pos_x() % 2 == 0:
        if get_pos_y() < get_world_size() - 1:
            move(North)
    else:
        if get_pos_y() > 0:
            move(South)


# 扫描单列
def scan_line():
    if get_pos_y() < get_world_size() - 1:
        move(North)


# 优雅清空农场
def clear_gently(force_soil=False):
    move_origin()
    for i in range(get_world_size()):
        for j in range(get_world_size()):
            if can_harvest():
                harvest()
            # 坏南瓜通过耕地移除
            if get_entity_type() == Entities.Dead_Pumpkin:
                till()
            # 是否强制耕地成土地
            if force_soil and get_ground_type() != Grounds.Soil:
                till()
            move(North)
        move(East)


# 浇水
def water():
    # 一罐水0.25，所以等当前田地含水量不高于一罐水时就浇水
    if num_items(Items.Water) > 0 and get_water() <= .75:
        use_item(Items.Water)
