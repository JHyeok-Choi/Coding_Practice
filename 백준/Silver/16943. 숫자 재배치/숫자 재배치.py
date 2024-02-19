import itertools

A, B = map(int, input().split())
C = -1
table = [int(''.join(i)) for i in itertools.permutations(str(A)) if i[0] is not '0']

for i in table:
    if i < B:
        C = C if C > i else i

print(C)