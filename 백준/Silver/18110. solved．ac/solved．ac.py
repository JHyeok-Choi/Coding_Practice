import sys

inp = sys.stdin.readline
n = int(inp())

# round == 오사오입
def rnd(x):
    if x - (x // 1) >= 0.5:
        return int(x) + 1
    else:
        return int(x)

if n:
    table = sorted([int(inp()) for _ in range(n)])
    num = rnd(n * 0.15)
    print(rnd(sum(table[num: n - num]) / len(table[num: n - num])))
else:
    print(0)