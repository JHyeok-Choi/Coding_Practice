import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N, K = map(int, input().split())
A = input().split()

def factorial(n):
    return n * factorial(n - 1) if n > 1 else 1

print((factorial(N) // factorial(N - K) // factorial(K) * 2 ** (K - 1)) % (10 ** 9 + 7))