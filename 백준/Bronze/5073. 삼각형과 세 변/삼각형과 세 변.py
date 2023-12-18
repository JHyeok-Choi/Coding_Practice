import sys
inp = sys.stdin.readline

while True:
    A, B, C = map(int, inp().split())
    if A == B == C == 0:
        break
    elif sum((A, B, C)) - max(A, B, C) <= max(A, B, C):
        print('Invalid')
    elif A == B == C:
        print('Equilateral')
    elif A == B or A == C or B == C:
        print('Isosceles')
    else:
        print('Scalene')