import z3
with open("Day10_input.txt", "r") as f:
    p1 = 0
    p2 = 0
    for row in f:
        wirings = []
        wirings_int = []
        print(row)
        for i in row.strip().split():
            if i[0] == "[":
                indicator_str = "".join(["1" if j == "#" else "0" for j in i[1:-1]])
                indicator = [j == "1" for j in indicator_str]
            elif i[0] == "(":
                wiring_str = [str(j) in i[1:-1].split(",") for j in range(len(indicator_str))]
                wiring_int = [int(j) for j in i[1:-1].split(",")]
                wirings.append(wiring_str)
                wirings_int.append(wiring_int)
            elif i[0] == "{":
                joltage_requirements = [int(j) for j in i[1:-1].split(",")]

        if indicator in wirings:
            p1 += 1
        else:
            current_wirings = wirings.copy()
            new_wirings = []
            already_seen = wirings.copy()
            c = 2
            while True:
                for i in wirings:
                    for j in current_wirings:
                        to_add = [not i_w if j_w else i_w for i_w, j_w in zip(i, j)]
                        if to_add not in already_seen:
                            new_wirings.append(to_add)
                            already_seen.append(to_add)
                if indicator in new_wirings:
                    p1 += c
                    break
                c += 1
                current_wirings = new_wirings.copy()
        o = z3.Optimize()
        vars = z3.Ints(f"n{i}" for i in range(len(wirings_int)))
        for var in vars: o.add(var>=0)
        for i, joltage in enumerate(joltage_requirements):
            equation = 0
            for b, button in enumerate(wirings_int):
                if i in button:
                    equation += vars[b]
            o.add(equation == joltage)
        o.minimize(sum(vars))
        o.check()
        p2 += (o.model().eval(sum(vars)).as_long())

    print(p1, p2)


