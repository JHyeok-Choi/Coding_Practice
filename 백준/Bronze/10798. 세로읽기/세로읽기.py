import sys
inp = sys.stdin.readline

table = [inp().rstrip() for i in range(5)]

for j in range(max(len(k) for k in table)):
    for l in range(5):
        if j < len(table[l]):
            print(table[l][j], end='')