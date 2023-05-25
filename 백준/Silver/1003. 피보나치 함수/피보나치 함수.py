import sys

inp = sys.stdin.readline
table = {0:0, 1:1, 2:1}
line = [int(inp()) for _ in range(int(inp()))]

for i in range(max(line) + 1):
    if i not in table:
        table[i] = table[i - 1] + table[i - 2]

for j in line:
    if j == 0:
        print(1, 0)
    elif j == 1:
        print(0, 1)
    else:
        print(table[j - 1], table[j])