from itertools import permutations

N, M = map(int, input().split())
table = list(map(int, input().split()))

for j in sorted(set([i for i in permutations(table, M)])):
    print(*j)
