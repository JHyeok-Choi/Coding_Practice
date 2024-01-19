import sys
input = sys.stdin.readline

# LIS

N = int(input())
bbiyak = [int(input()) for _ in range(N)]
dp = [0] * N

for i in range(N):
    mx = 0
    for j in range(i):
        if bbiyak[i] > bbiyak[j]:
            mx = max(mx, dp[j])
    dp[i] = mx + 1

print(N - max(dp))