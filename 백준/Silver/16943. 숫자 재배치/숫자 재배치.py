import itertools

A, B = map(int, input().split())
C = -1
table = [''.join(i) for i in itertools.permutations(str(A))]

for i in table:
    if i[0] == '0':
        continue

    i = int(i)

    if i < B:
        C = C if C > i else i

print(C)