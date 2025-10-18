import carrot
import grass
import sunflower
import tree
import utils
from __builtins__ import *

plant_list = [
    grass.line,
    grass.line,
    tree.line,
    tree.line,
    carrot.line,
    carrot.line,
    sunflower.line,
    sunflower.line,
]


def main():
    # 清空农场
    utils.clear_gently()

    # 种植和收获
    while True:
        for i in range(get_world_size()):
            plant_list[i]()
            move(East)


if __name__ == '__main__':
    main()
