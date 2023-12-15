import sys
inp = sys.stdin.readline

P = int(inp())

for _ in range(P):
    line = list(map(int, inp().split()))
    count = 0

    for i in range(1, len(line) - 1):
        for j in range(1 + i, len(line)):
            if line[i] > line[j]:
                line[i], line[j] = line[j], line[i]
                count += 1
    print(line[0], count)