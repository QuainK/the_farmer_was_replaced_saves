import utils
from __builtins__ import *

# 奇异物质数量阈值，高于它才使用，等于低于它就得用施肥去获取
weird_limit = 2000


# 单格
def one():
    if can_harvest():
        harvest()
    plant(Entities.Sunflower)
    utils.water()
    # 奇异物质不够用了，就开始施肥并收获
    if num_items(Items.Weird_Substance) <= weird_limit:
        if num_items(Items.Fertilizer) > 0:
            use_item(Items.Fertilizer)


# 收获和种植一列
def plant_column():
    utils.move_to(get_pos_x(), 0)
    for _ in range(get_world_size()):
        one()
        utils.scan_column()


# 感染一列
def weird_column():
    # 十字形错位布局
    for _ in range(get_world_size()):
        if get_pos_x() % 4 != 1 and get_pos_x() % 4 != 3:
            break
        else:
            if get_pos_x() % 4 == 1 and get_pos_y() % 3 == 1:
                use_item(Items.Weird_Substance)
            elif get_pos_x() % 4 == 3 and get_pos_y() % 3 == 2:
                use_item(Items.Weird_Substance)
            utils.scan_column()


# 整场
def main():
    utils.clear_gently(True)
    while True:
        utils.multiple(plant_column)
        # 奇异物质够用，就开始感染作物并收获
        if num_items(Items.Weird_Substance) > weird_limit:
            utils.multiple(weird_column)


if __name__ == '__main__':
    main()
