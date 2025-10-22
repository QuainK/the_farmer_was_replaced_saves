import carrot
import grass
import sunflower
import tree
import utils
from __builtins__ import *


def main():
    utils.clear_gently()
    # 按列混合种植基础作物
    plant_list = [
        grass.column,
        tree.column,
        carrot.column,
        sunflower.column,
    ]
    while True:
        for column_func in plant_list:
            # 无人机多线程处理列
            utils.multiple_column(column_func)
            do_a_flip()


if __name__ == '__main__':
    main()
