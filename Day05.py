with open("Day05_input.txt", "r") as f:
    p1 = 0
    ranges = []
    for row in f:
        if row.strip() == "":
            break
        startR,endR = [int(i) for i in row.strip().split("-")]
        added = False
        while not added:
            for i, (startOld, endOld) in enumerate(ranges):
                if startR <= startOld <= endR <= endOld:
                    ranges.remove(ranges[i])
                    startR = startR
                    endR = endOld
                    break
                if startOld <= startR <= endR <= endOld:
                    added = True
                    break
                if startR <= startOld <= endOld <= endR:
                    ranges.remove(ranges[i])
                    startR = startR
                    endR = endR
                    break
                if startOld <= startR <= endOld <= endR:
                    ranges.remove(ranges[i])
                    startR = startOld
                    endR = endR
                    break
            else:
                added = True
                ranges.append((startR, endR))
    for row in f:
        row = int(row.strip())
        for start, end in ranges:
            if start <= row <= end:
                p1 += 1
                break
    print(p1)
    print(sum([end - start + 1 for start, end in ranges]))