import sys

print(*sorted(map(int, sys.stdin.read()[::-1].split()[:-1])))