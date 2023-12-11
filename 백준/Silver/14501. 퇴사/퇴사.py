import sys
inp = sys.stdin.readline

N = int(inp())

table = [list(map(int, inp().split())) for i in range(N)]

pay = [0 for i in range(N + 1)]

for i in range(N):
    for j in range(i + table[i][0], N + 1):
        if pay[j] < pay[i] + table[i][1]:
            pay[j] = pay[i] + table[i][1]

print(pay[-1])