from itertools import combinations_with_replacement

N, M = map(int, input().split())
table = sorted(set(map(int, input().split())))

[print(*i) for i in combinations_with_replacement(table, M)]