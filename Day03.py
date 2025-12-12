def find_joltage(s, l): return max(s) if l == 1 else max(s[:-l+1]) + find_joltage(s[s.index(max(s[:-l+1]))+1:],l-1)
with open("Day03_input.txt", "r") as f:
    print(sum([int(find_joltage([i for i in row.strip()],2)) for row in f]))
with open("Day03_input.txt", "r") as f:
    print(sum([int(find_joltage([i for i in row.strip()],12)) for row in f]))


