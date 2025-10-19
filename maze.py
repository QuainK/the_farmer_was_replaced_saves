from __builtins__ import *


def main():
    clear()
    while True:
        plant(Entities.Bush)
        # substance = get_world_size() * 2 ** (num_unlocked(Unlocks.Mazes) - 1)
        substance = 4
        use_item(Items.Weird_Substance, substance)
        if get_entity_type() == Entities.Treasure:
            harvest()


if __name__ == '__main__':
    main()
