import sys

n = int(input())

# round == 오사오입
def rnd(x):
    if x % 1 >= 0.5:
        return int(x) + 1
    else:
        return int(x)

if n:
    table = sorted(list(map(int, sys.stdin.read().split())))
    num = rnd(n * 0.15)
    print(rnd(sum(table[num: n - num]) / len(table[num: n - num])))
else:
    print(0)