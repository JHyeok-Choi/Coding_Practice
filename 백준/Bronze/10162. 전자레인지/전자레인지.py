T = int(input())
s = [300, 60, 10]
cnt = [0, 0, 0]

for i, j in enumerate(s):
    cnt[i] = T // j
    T = T % j

print(*cnt if T == 0 else [-1])