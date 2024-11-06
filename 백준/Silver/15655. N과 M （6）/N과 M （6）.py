from itertools import combinations

N, M = map(int, input().split())
table = sorted(map(int, input().split()))

for i in combinations(table, M):
    print(*i)