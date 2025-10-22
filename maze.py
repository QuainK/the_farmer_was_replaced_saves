import utils
from __builtins__ import *


# 单格
def one():
    while True:
        plant(Entities.Bush)
        # 加成倍率
        times = 2 ** (num_unlocked(Unlocks.Mazes) - 1)
        # 就种单格
        # substance = get_world_size() * times
        substance = 1 * times
        if num_items(Items.Weird_Substance) > 0:
            use_item(Items.Weird_Substance, substance)
        else:
            if can_harvest():
                harvest()
        if get_entity_type() == Entities.Treasure:
            harvest()


# 整场
def main():
    utils.clear_gently(True)
    while True:
        utils.multiple_column(one)


if __name__ == '__main__':
    main()
