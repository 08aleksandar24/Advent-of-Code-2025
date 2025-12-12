with open("Day09_input.txt", "r") as f:
    coordinates = []
    part1 = 1
    p2 = 0
    for row in f:
        coordinates.append(tuple(int (i) for i in row.strip().split(",")))
    print(coordinates)
    d = {}
    for i, (x1,y1) in enumerate(coordinates):
        for j, (x2,y2) in enumerate(coordinates[i+1:]):
            d[i,i+j+1] = (abs(x1-x2)+1)*(abs(y1-y2)+1)
    p1 = max(d.items(), key=lambda x: x[1])
    print(p1)

for (i,j), p2 in sorted(d.items(), key=lambda x: x[1], reverse=True):
    (x1,y1), (x2,y2) = coordinates[i], coordinates[j]
    xmin = min(x1, x2)
    xmax = max(x1, x2)
    ymin = min(y1, y2)
    ymax = max(y1, y2)
    inside = True
    for(x3,y3),(x4,y4) in zip(coordinates, coordinates[1:] + [coordinates[0]]):
        if y3 == y4 and ymin<y3<ymax:
            x2min = min(x3, x4)
            x2max = max(x3, x4)
            if (x2min <= xmin <= x2max) or (x2min <= xmax <= x2max):
                inside = False
                break

        if x3 == x4 and xmin<x3<xmax:
            y2min = min(y3, y4)
            y2max = max(y3, y4)
            if (y2min <= ymin <= y2max) or (y2min <= ymax <= y2max):
                inside = False
                break
    if inside:
        print(p2)
        break
