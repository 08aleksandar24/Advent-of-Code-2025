import numpy as np
with open("Day04_input.txt", "r") as f:
    map = []
    for row in f:
        row = [1 if i =="@" else 0 for i in "."+row.strip()+"."]
        map.append(row)
    line = [0 for i in map[0]]
    map.append(line)
    map.insert(0,line)
    map = np.array(map)
    p1 = 0
    remove = []
    for i in range(1,len(map)-1):
        for j in range(1,len(map[i])-1):
            if map[i][j] == 1 and sum([map[i+k][j+l] for k in range(-1,2) for l in range(-1,2)])<=4:
                p1+=1
                remove.append([i,j])
    for i,j in remove:
        map[i][j] = 0
    print(len(remove))
    p2 = p1
    add = -1
    while add != 0:
        remove = []
        for i in range(1, len(map) - 1):
            for j in range(1, len(map[i]) - 1):
                if map[i][j] == 1 and sum([map[i + k][j + l] for k in range(-1, 2) for l in range(-1, 2)]) <= 4:
                    remove.append([i,j])
        for i, j in remove:
            map[i][j] = 0
        add = len(remove)
        p2 += add
    print(p2)


