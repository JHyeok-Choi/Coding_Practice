import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N, K = map(int, input().split())

def factorial(n):
    return n * factorial(n - 1) if n > 1 else 1

def combination(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))

print(combination(N + K - 1, N) % 10 ** 9)