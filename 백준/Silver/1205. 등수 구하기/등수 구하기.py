N, T, P = map(int, input().split())

if N == 0:
    print(1)
else:
    score = list(map(int, input().split()))
    if N == P and T <= score[-1]:
        print(-1)
    else:
        for i in range(N):
            rank = N + 1
            if T >= score[i]:
                rank = i + 1
                break
        
        print(rank)