import sys

for i in list(map(int, sys.stdin.read().split()))[:-1]:
    strS = bin(i - 1)[2:][::-1]
    table = [3 ** j for j in list(filter(lambda x: strS[x] == '1', range(len(strS))))]
    if len(table) == 0:
        print('{ }')
    else:
        print('{ ' + str(table)[1:-1] + ' }')