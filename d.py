list = [2,4,543,436,4,4223,424142,1]
for i in range(len(list), -1, -1):
    if list[i] == 4:
        list.pop()