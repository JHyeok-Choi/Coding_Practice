import sys
inp = sys.stdin.readline

N = int(inp())
P = sorted(list(map(int, inp().split())))

count = 0
for i in range(N):
    count = count + sum(P[:i+1])

print(count)