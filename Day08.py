with open("Day08_input.txt", "r") as f:
    coordinates = []
    part1 = 1
    p2 = 0
    for row in f:
        coordinates.append(tuple(int (i) for i in row.strip().split(",")))
    print(coordinates)
    d = {}
    for i, (x1,y1,z1) in enumerate(coordinates):
        for j, (x2,y2,z2) in enumerate(coordinates[i+1:]):
            d[i,i+j+1] = (x1-x2)**2+(y1-y2)**2+(z1-z2)**2
    sorted_d = sorted(d.items(), key=lambda x: x[1])
    d2 = {i:set([i]) for i in range(len(coordinates))}
    print([(coordinates[i], coordinates[j]) for (i,j),k in sorted_d])
    for iteration, ((p1,p2), _) in enumerate(sorted_d):
        if iteration >= 1000:
            break
        circuit = d2[p1].union(d2[p2])
        for i in circuit:
            d2[i] |= circuit

    sorted_results = sorted(d2.items(), key=lambda x: len(x[1]), reverse=True)
    cleaned_results = {}
    already_added = []
    c = 0
    for i,j in sorted_results:
        if i not in already_added:
            c += 1
            part1 *= len(j)
            print(len(j))
            if c == 3:
                break
        already_added.extend(j)
    print(part1)


with open("Day08_input.txt", "r") as f:
    coordinates = []
    part1 = 1
    p2 = 0
    for row in f:
        coordinates.append(tuple(int (i) for i in row.strip().split(",")))

    d = {}
    for i, (x1,y1,z1) in enumerate(coordinates):
        for j, (x2,y2,z2) in enumerate(coordinates[i+1:]):
            d[i,i+j+1] = (x1-x2)**2+(y1-y2)**2+(z1-z2)**2
    sorted_d = sorted(d.items(), key=lambda x: x[1])
    d2 = {i:set([i]) for i in range(len(coordinates))}

    for iteration, ((p1,p2), _) in enumerate(sorted_d):
        circuit = d2[p1].union(d2[p2])
        if len(circuit) == len(coordinates):
            print(coordinates[p1][0]*coordinates[p2][0])
            break
        for i in circuit:
            d2[i] |= circuit


