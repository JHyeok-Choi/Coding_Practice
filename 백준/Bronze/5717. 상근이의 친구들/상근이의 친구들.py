import sys
inp = sys.stdin.readline
M, F = map(int, inp().split())

while M:
    print(M + F)
    M, F = map(int, inp().split())