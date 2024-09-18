from itertools import permutations

_, M = map(int, input().split())

[print(*i) for i in permutations(sorted(map(int, input().split())), M)]