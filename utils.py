from __builtins__ import *


# 移动到指定坐标
def move_to(x=0, y=0):
    while x != get_pos_x() or y != get_pos_y():
        # 判断当前位置和目标位置的距离，并向目标位置移动
        # 如果距离超过地图尺寸的一半，那说明正向比反向更远，所以需要反向移动，更节省路程
        delta_x = x - get_pos_x()
        delta_y = y - get_pos_y()
        size = get_world_size()
        if delta_x > 0:
            if abs(delta_x) < size / 2:
                move(East)
            else:
                move(West)
        elif delta_x < 0:
            if abs(delta_x) < size / 2:
                move(West)
            else:
                move(East)
        elif delta_y > 0:
            if abs(delta_y) < size / 2:
                move(North)
            else:
                move(South)
        elif delta_y < 0:
            if abs(delta_y) < size / 2:
                move(South)
            else:
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


# 单列定向扫描
def scan_column():
    if get_pos_y() < get_world_size() - 1:
        move(North)


# 单行定向扫描
def scan_row():
    if get_pos_x() < get_world_size() - 1:
        move(East)


# 优雅清空农场
def clear_gently(force_soil=False):
    # 收获全场已有作物
    def harvest_line():
        for _ in range(get_world_size()):
            if can_harvest():
                harvest()
            # 坏南瓜通过耕地移除
            if get_entity_type() == Entities.Dead_Pumpkin:
                till()
            # 是否强制耕地成土地
            if force_soil and get_ground_type() != Grounds.Soil:
                till()
            scan_column()

    move_origin()
    # 多线程收获
    multiple_column(harvest_line)
    move_origin()


# 浇水
def water():
    # 一罐水0.25，所以等当前田地含水量不高于一罐水时就浇水
    if num_items(Items.Water) > 0 and get_water() <= .75:
        use_item(Items.Water)


# 无人机多线程处理列
def multiple_column(func):
    for _ in range(get_world_size()):
        if num_drones() < max_drones():
            # 能派出子无人机，就让子无人机执行
            spawn_drone(func)
        else:
            # 子无人机派完了，主无人机亲自执行，此时线程数最大
            func()
            move_to(get_pos_x(), 0)
        # 一列一列派出子无人机
        scan_row()
    move_origin()


# 无人机多线程处理行
def multiple_row(func):
    for _ in range(get_world_size()):
        if num_drones() < max_drones():
            spawn_drone(func)
        else:
            func()
            move_to(0, get_pos_y())
        scan_column()
    move_origin()
