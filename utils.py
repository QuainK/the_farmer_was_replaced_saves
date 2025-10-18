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


# 优雅清空农场
def clear_gently():
    move_origin()
    for i in range(get_world_size()):
        for j in range(get_world_size()):
            if can_harvest():
                harvest()
            move(North)
        move(East)
