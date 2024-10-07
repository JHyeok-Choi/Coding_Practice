import sys
inp = sys.stdin.readline

N, K = map(int, inp().split())
table = list(map(int, inp().split()))
origin = sum(table[:K])
tmp = origin

for i in range(N - K):
    tmp += table[i + K] - table[i]
    if origin < tmp:
        origin = tmp

print(origin)