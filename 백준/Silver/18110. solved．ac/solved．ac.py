import sys

n = int(sys.stdin.readline())

if n:
    table = sorted(map(int, sys.stdin.read().split()))
    num = (n * 3 + 10) // 20
    print(int(sum(table[num: n - num]) / (n - num * 2) + .5))
else:
    print(0)