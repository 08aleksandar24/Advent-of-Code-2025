with open("Day12_input.txt", "r") as f:
    p1 = 0
    for row in f:
        row = row.strip()
        if row != "" and row[-1] != ":" and ":" in row:
            size, boxes = row.split(":")
            sizeX, sizeY = [int(i) for i in size.split("x")]
            print(sizeX, sizeY, boxes)
            boxesSize = sum([int(i) for i in boxes.split()])
            if sizeX*sizeY >= boxesSize*3*3:
                p1 += 1

    print(p1)