import sys
input = sys.stdin.readline

N, M = map(int, input().split())
AM = [list(map(int, input().split())) for _ in range(N)]
M, K = map(int, input().split())
BK = [list(map(int, input().split())) for _ in range(M)]

for i in range(N):
    table = []
    for j in range(K):
        num = 0
        for k in range(M):
            num += AM[i][k] * BK[k][j]
        table.append(num)
    print(*table)