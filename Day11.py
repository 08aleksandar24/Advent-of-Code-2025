from functools import cache

import networkx as nx
with open("Day11_input.txt", "r") as f:
    G = nx.DiGraph()
    d = {}
    for row in f:
        k, v = row.split(":")
        v = v.strip().split()
        d[k] = v
        for point in v:
            G.add_edge(k, point)
    print(len(list(nx.all_simple_paths(G, source='you', target='out'))))
    # PART 2 needs optimization
    @cache
    def numberOfWays(fromPoint, toPoint):
        if fromPoint == toPoint:
            return 1
        if fromPoint not in d:
            return 0
        return sum(numberOfWays(newFromPoint, toPoint) for newFromPoint in d[fromPoint])
    print("part1", numberOfWays("you", "out"))
    print("part2", numberOfWays("svr", "fft") * numberOfWays("fft", "dac") * numberOfWays("dac", "out") )