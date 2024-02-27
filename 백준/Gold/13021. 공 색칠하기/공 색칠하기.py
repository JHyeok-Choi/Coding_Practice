N, M = map(int, input().split())
table = [0] * (N + 1)

for i in range(1, M + 1):
    L, R = map(int, input().split())
    table[L: R + 1] = [i] * (R - L + 1)

print(2 ** len(set(table) - {0}))