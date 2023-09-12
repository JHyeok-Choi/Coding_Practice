N, M = map(int, input().split())
for i in range(N):
    x = list(input())
    print(*list(reversed(x)), sep='')