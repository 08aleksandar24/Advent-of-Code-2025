with open("Day01_input.txt", "r") as f:
    start = 50
    total_zero = 0
    total_zero_touches = 0
    for row in f:
        r = row.strip()
        print(start, r)
        if start == 0:
            total_zero += 1
            if r[0] == "L":
                start = 100
        if r[0] == "L":
            total_zero_touches += -1 * ((start - int(r[1:])-1) // 100)
            print(-1 * ((start - int(r[1:])-1) // 100))
            start = (start - int(r[1:])) % 100
        else:
            print(((start + int(r[1:])) // 100))
            total_zero_touches += ((start + int(r[1:])) // 100)
            start = (start + int(r[1:])) % 100


    print("Final:", start)
    print("total_zero:", total_zero)
    print("total_zero_touches:", total_zero_touches)
