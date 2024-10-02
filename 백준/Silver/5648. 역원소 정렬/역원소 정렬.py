import sys

n, *m = sys.stdin.read().split()
print(*sorted([int(i[::-1]) for i in m]), sep='\n')