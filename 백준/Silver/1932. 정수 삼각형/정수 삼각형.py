n = int(input())
table = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    for j in range(len(table[i])):
        if j == 0:
            table[i][j] += table[i - 1][j]
        elif j == i:
            table[i][j] += table[i - 1][j - 1]
        else:
            table[i][j] += max(table[i - 1][j], table[i - 1][j - 1])

print(max(table[-1]))