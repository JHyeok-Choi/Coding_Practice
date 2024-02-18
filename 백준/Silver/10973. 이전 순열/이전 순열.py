import sys
input = sys.stdin.readline

N = int(input())
perm = list(map(int, input().split()))

for i in range(N - 1, 0, -1):
    if perm[i - 1] > perm[i]:
        for j in range(N - 1, 0, -1):
            if perm[i - 1] > perm[j]:
                perm[i - 1], perm[j] = perm[j], perm[i - 1]
                perm = perm[:i] + sorted(perm[i:], reverse=True)
                print(*perm)
                exit()

print(-1)