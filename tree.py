import utils
from __builtins__ import *


def main():
    # 清空农场
    utils.clear_gently()
    while True:
        for i in range(get_world_size()):
            for j in range(get_world_size()):
                if can_harvest():
                    harvest()
                if (i + j) % 2 == 0:
                    plant(Entities.Tree)
                move(North)
            move(East)


if __name__ == '__main__':
    main()
