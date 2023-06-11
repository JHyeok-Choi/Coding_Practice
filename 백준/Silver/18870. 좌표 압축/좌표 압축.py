import sys
inp = sys.stdin.readline

N = int(inp())
X = list(map(int, inp().split()))
Xp = sorted(set(X))
Xd = dict()

for i, j in enumerate(Xp):
    Xd[j] = i

for k in X:
    print(Xd[k], end=" ")