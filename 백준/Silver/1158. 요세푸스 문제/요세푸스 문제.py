N, K = map(int, input().split())
table = [i for i in range(1, N + 1)]
answer = "<"
tmp = 0

for _ in range(N):
    tmp += K - 1
    if tmp >= len(table):
        tmp = tmp % len(table)
    answer += f"{table.pop(tmp)}, "

print(answer[:-2] + ">")