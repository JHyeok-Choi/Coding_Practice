import sys
inp = sys.stdin.readline

N, M = map(int, inp().split())
memo = dict()

for _ in range(N):
    address, password = inp().split()
    memo[address] = password

sys.stdout.write("\n".join([memo[inp().rstrip()] for _ in range(M)]))