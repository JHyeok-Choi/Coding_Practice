import sys

S = list(map(int, sys.stdin.read().split()))[:-1]
s = s = [3 ** i for i in range(64)]

for i in S:
    strS = bin(i - 1)[2:][::-1]
    table = [s[j] for j in list(filter(lambda x: strS[x] == '1', range(len(strS))))]
    if len(table) == 0:
        print('{ }')
    else:
        print('{ ' + str(table)[1:-1] + ' }')