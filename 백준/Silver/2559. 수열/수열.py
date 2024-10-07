N, K = map(int, input().split())
table = list(map(int, input().split()))
origin = sum(table[:K])
tmp = origin

for i in range(N - K):
    tmp += table[i + K] - table[i]
    if origin < tmp:
        origin = tmp

print(origin)