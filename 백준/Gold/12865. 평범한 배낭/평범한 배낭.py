import sys
input = sys.stdin.readline

N, K = map(int, input().split())
table = [tuple(map(int, input().split())) for _ in range(N)]
dp = [0] * (K + 1)

for i in table:
    for j in range(K, i[0] - 1, -1):
        dp[j] = max(dp[j], dp[j - i[0]] + i[1])

print(dp[-1])