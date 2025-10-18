from __builtins__ import *


def main():
    clear()
    while True:
        for i in range(get_world_size()):
            for j in range(get_world_size()):
                if can_harvest():
                    harvest()
                if get_ground_type() != Grounds.Soil:
                    till()
                plant(Entities.Carrot)
                move(North)
            move(East)


if __name__ == '__main__':
    main()
