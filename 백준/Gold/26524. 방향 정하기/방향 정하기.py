n = int(input())
answer = 1

for i in range(1, 1 + n):
    answer = (answer * i) % (10 ** 9 + 7)

print(answer)