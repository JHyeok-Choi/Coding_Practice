import sys

text = sys.stdin.read()
table = dict()

for i in text:
    if i not in ['\n', ' ']:
        if i not in table:
            table[i] = 1
        else:
            table[i] += 1

for idx, cnt in dict(sorted(table.items())).items():
    if cnt == max(table.values()):
        print(idx, end='')