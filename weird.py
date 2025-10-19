import utils
from __builtins__ import *


def main():
    clear()
    do_a_flip()
    while True:
        utils.move_origin()
        for i in range(get_world_size()):
            if (get_pos_x() % 3) != 1:
                move(East)
                continue
            for j in range(get_world_size()):
                if get_pos_x() % 3 == 1 and get_pos_y() % 3 == 1:
                    use_item(Items.Weird_Substance)
                move(North)
            move(East)

        utils.move_origin()
        for i in range(get_world_size()):
            for j in range(get_world_size()):
                if can_harvest():
                    harvest()
                # Z字形扫描
                utils.z_scan()
            move(East)


if __name__ == '__main__':
    main()
