T = int(input())

for test_case in range(1, T + 1):
    count = 0
    num = 97
    alpha = input()
    for i in alpha:
        if i == chr(num):
            count += 1
        else:
            break
        num += 1
    print(f'#{test_case}', count)