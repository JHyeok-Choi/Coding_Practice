import sys
input = sys.stdin.readline

T = int(input())
N = [int(input()) for i in range(T)]

P = [1] * 3 + [0] * (max(N) - 3 if max(N) > 3 else 0)

for i in range(3, max(N)):
    P[i] = P[i - 2] + P[i - 3]

for j in N:
    print(P[j - 1])