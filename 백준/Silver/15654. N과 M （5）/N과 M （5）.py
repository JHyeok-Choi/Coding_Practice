from itertools import permutations

_, M = map(int, input().split())

for i in permutations(sorted(map(int, input().split())), M):
    print(*i)