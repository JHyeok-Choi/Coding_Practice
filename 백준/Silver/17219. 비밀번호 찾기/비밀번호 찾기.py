import sys
inp = sys.stdin.readline

N, M = map(int, inp().split())
memo = {}

for i in range(N):
    address, password = map(str, inp().split())
    memo[address] = password

sys.stdout.write("\n".join([memo[inp().rstrip()] for _ in range(M)]))