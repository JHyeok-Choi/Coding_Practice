N = int(input())
answer = []

for i in range(N):
    tmp = input()
    if i == 0:
        answer = list(tmp)
    for j, k in enumerate(tmp):
        if answer[j] != k:
            answer[j] = '?'

print(''.join(answer))