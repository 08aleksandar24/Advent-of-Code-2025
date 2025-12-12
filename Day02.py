r1 = []
r2 = []
with open("Day02_input.txt", "r") as f:
    p1 = 0
    for row in f:
        row = row.strip().split(",")
        for id_range in row:
            start, end = id_range.split("-")

            for times in range(2, max(len(start),len(end))+1):

                new_start = start
                new_end = end
                while len(new_start) % times != 0:
                    new_start = str(10 ** len(new_start))
                while len(new_end) % times != 0:
                    new_end = str(10 ** (len(new_end)-1)-1)
                #print(2,start,end)
                start_check = int(new_start[:len(new_start)//times])
                end_check = int(new_end[:len(new_end)//times])


                #print(3,start_check,end_check)
                for i in range(start_check, end_check+1):
                    double_i = int(str(i)*times)
                    if int(start)<=double_i<=int(end):
                        p1 += double_i
                        if(times) == 2:
                            r1.append(double_i)
                        r2.append(double_i)
    print(sum(r1))
    print(sum(set(r2)))
