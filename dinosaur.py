import utils
from __builtins__ import *


def main():
    change_hat(Hats.Purple_Hat)
    utils.clear_gently(True)
    # 哈密顿回路扫描
    while True:
        change_hat(Hats.Purple_Hat)
        utils.move_origin()
        change_hat(Hats.Dinosaur_Hat)
        move(North)
        while get_pos_x() != 0 or get_pos_y() != 0:
            if get_pos_x() % 2 == 0 and get_pos_y() < get_world_size() - 1:
                if not move(North):
                    break
            elif get_pos_x() % 2 == 1 and get_pos_y() > 1:
                if not move(South):
                    break
            elif get_pos_x() == get_world_size() - 1 and get_pos_y() == 1:
                if not move(South):
                    break
                back_fail = False
                while get_pos_x() > 0:
                    if not move(West):
                        back_fail = True
                        break
                if back_fail:
                    break
            else:
                if not move(East):
                    break
            move(North)


if __name__ == '__main__':
    main()
