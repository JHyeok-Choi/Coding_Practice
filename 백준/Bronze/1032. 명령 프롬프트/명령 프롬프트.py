N = int(input())
answer = list(input())

for i in range(N - 1):
    tmp = input()
    for j, k in enumerate(tmp):
        if answer[j] != k:
            answer[j] = '?'

print(''.join(answer))