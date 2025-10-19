from __builtins__ import *


def harvest_column():
    for _ in range(get_world_size()):
        harvest()
        move(North)


def main():
    clear()
    while True:
        if spawn_drone(harvest_column):
            move(East)
            harvest_column()
            move(East)


if __name__ == '__main__':
    main()
