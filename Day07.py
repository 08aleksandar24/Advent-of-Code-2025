with open("Day07_input.txt", "r") as f:
    r = set()
    r2 = {}
    p1 = 0
    p2 = 0
    for row in f:
        if 'S' in row:
            start_point = row.index('S')
            r.add(start_point)
            r2[start_point] = 1
        else:
            new_r = set()
            for i in r:
                if row[i] == '^':
                    new_r.add(i-1)
                    new_r.add(i+1)
                    if i-1 in r2:
                        r2[i - 1] += r2[i]
                    else:
                        r2[i-1] = r2[i]
                    if i+1 in r2:
                        r2[i+1] += r2[i]
                    else:
                        r2[i+1] = r2[i]
                    r2[i] = 0
                    p1 += 1
                else:
                    new_r.add(i)
            r = new_r
            p2 += len(r2)
            for i,c in enumerate(row):
                if c == '^':
                    print("^",end="")
                elif i in r2 and r2[i] > 0:
                    print("|",end="")
                else:
                    print(" ",end="")
            print()
    print(p1)
    print(sum(r2.values()))
