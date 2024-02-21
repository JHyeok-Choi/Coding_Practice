#  D(n) = D(n - 1) + 2 * D(n - 2)

N = int(input())

d, d[0], d[1] = [0] * (N + 1), 1, 1
n = 2

while n < N + 1:
    d[n] = d[n - 1] + 2 * d[n - 2]
    n += 1

if N % 2 == 0:
    print((d[N] + d[N // 2] + 2 * d[(N - 2) // 2]) // 2)
else:
    print((d[N] + d[(n - 1) // 2]) // 2)