N = int(input())
t = [0, 1, 3]

for i in range(3, 1001):
    t.append(t[i - 2]*2 + t[i - 1])

print(t[N] % 10007)