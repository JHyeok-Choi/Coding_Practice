N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())
count = N

for i in A:
    i -= B
    if i > 0:
        if i % C:
            count += (i // C) + 1
        else:
            count += i // C

print(count)