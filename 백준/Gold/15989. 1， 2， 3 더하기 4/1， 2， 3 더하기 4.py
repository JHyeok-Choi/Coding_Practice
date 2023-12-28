import sys
input = sys.stdin.readline

T = int(input())

n_case = [1] * 10001

for i in range(2, 10001):
    n_case[i] += n_case[i - 2]

for j in range(3, 10001):
    n_case[j] += n_case[j - 3]

for _ in range(T):
    n = int(input())
    print(n_case[n])