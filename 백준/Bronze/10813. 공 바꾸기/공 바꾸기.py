import sys

inp = sys.stdin.readline

N, M = map(int, inp().split())
table = [i for i in range(N+1)]

for _ in range(M):
    i, j = map(int, inp().split())
    table[i], table[j] = table[j], table[i]
    
print(*table[1:])