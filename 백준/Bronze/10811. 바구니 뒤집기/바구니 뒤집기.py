import sys
inp = sys.stdin.readline

N, M = map(int, inp().split())
table = [x for x in range(N+1)]

for _ in range(M):
    i, j = map(int, inp().split())
    table[i:j+1] = table[i:j+1][::-1]

print(*table[1:])