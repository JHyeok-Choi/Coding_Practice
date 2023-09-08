N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())
count = 0

for i in A:
    i -= B
    count += 1
    if i > 0:
        count += i // C
        i %= C
    if i > 0:
        count += 1

print(count)