import sys

text = sys.stdin.read()
table = dict()

for i in text:
    if i not in ['\n', ' ']:
        if i not in table:
            table[i] = 1
        else:
            table[i] += 1

table = dict(sorted(table.items()))

for idx, cnt in table.items():
    if cnt == max(table.values()):
        print(idx, end='')