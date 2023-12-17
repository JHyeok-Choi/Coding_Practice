import sys
inp = sys.stdin.readline

N, game = inp().split()

names = [inp().rstrip() for i in range(int(N))]
names = set(names)

numbers = {'Y': 1, 'F': 2, 'O': 3}

print(len(names) // numbers[game])