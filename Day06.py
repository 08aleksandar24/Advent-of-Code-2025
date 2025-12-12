import numpy as np

with open("Day06_input.txt", "r") as f:
    r = []
    for row in f:
        if "+" in row:
            operations = np.array(row.strip().split())
        else:
            r.append([int(i) for i in row.strip().split()])

    r = np.array(r, dtype=object)
    print(sum(np.prod(r[:, operations=="*"], axis=0))+sum(np.sum(r[:, operations=="+"], axis=0)))

with open("Day06_input.txt", "r") as f:
    r = {}
    p2 = 0
    for row in f:
        if "+" in row:
            for c in r:
                r[c] = int(r[c])
            print(r)
            for i,c in enumerate(row):
                if c == "*":
                    p = 1
                    while i in r:
                        p *= r[i]
                        i += 1
                    p2 += p
                elif c == "+":
                    p = 0
                    while i in r:
                        p += r[i]
                        i += 1
                    p2 += p
        else:
            for i,c in enumerate(row):
                if c.isdigit():
                    if i in r:
                        r[i] += c
                    else:
                        r[i] = c
    print(p2)