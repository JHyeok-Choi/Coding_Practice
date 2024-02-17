N = int(input())
A = list(map(int, input().split()))
table = dict()
tsq = 1

for i in A:
    if i not in table:
        table[i] = 1
    else:
        table[i] += 1

for i in table.values():
    tsq *= i + 1

print((tsq - 1) % (10**9 + 7))