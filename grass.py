from __builtins__ import *


def main():
    clear()
    while True:
        for i in range(get_world_size()):
            for j in range(get_world_size()):
                if can_harvest():
                    harvest()
                move(North)
            move(East)


if __name__ == '__main__':
    main()
