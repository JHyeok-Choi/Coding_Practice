N, K = map(int, input().split())
A = list(map(int, input().split()))

table = {0: 1}

hap = 0
answer = 0

for i in A:
    hap += i

    if hap - K in table:
        answer += table[hap - K]
    if hap in table:
        table[hap] += 1
    else:
        table[hap] = 1

print(answer)