N = int(input())
dN = list(map(int, input().split()))
table = [0 for _ in range(N)]
wait = 0

while sum(dN):
    for i, j in enumerate(dN):
        if j == 0:
            continue
        else:
            dN[i] -= 1
            wait += 1
            table[i] = wait

print(*table)