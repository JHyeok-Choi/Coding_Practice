N = int(input())
M = list(map(int, input().split()))

for i in range(N - 1, 0, -1):
    if M[i - 1] < M[i]:
        for j in range(N - 1, 0, -1):
            if M[i - 1] < M[j]:
                M[i - 1], M[j] = M[j], M[i - 1]
                M = M[:i] + sorted(M[i:])
                print(*M)
                exit()

print(-1)