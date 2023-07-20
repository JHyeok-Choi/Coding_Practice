import sys

inp = sys.stdin.readline

table = [list(map(int, inp().split())) for _ in range(9)]
top = 0
a, b = 0, 0

for i, j in enumerate(table):
    if top < max(j):
        top = max(j)
        a = i
        b = j.index(top)

print(top)
print(a+1, b+1)