import sys
input = sys.stdin.readline

T = int(input())
L = [int(input()) for _ in range(T)]
table = [0] * (max(L) + 1)
table[0] = 1

for i in range(2, max(L) + 1, 2):
    for j in range(2, i + 1, 2):
        table[i] += table[j - 2] * table[i - j]
    table[i] %= 1000000007

[print(table[i]) for i in L]