# 清空农场
clear()

# 耕地
for i in range(get_world_size()):
    for j in range(get_world_size()):
        till()
        move(North)
    move(East)

# 种植和收获
while True:
    # if can_harvest():
    #     harvest()
    for i in range(get_world_size()):
        for j in range(get_world_size()):
            if can_harvest():
                harvest()
            # if (i + j) % 2 == 0:
            #     plant(Entities.Tree)
            # plant(Entities.Bush)
            plant(Entities.Carrot)
            move(North)
        move(East)
