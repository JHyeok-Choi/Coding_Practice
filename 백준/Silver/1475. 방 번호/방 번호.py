N = map(int, input().replace('9', '6'))
table = [0] * 10

for i in N:
    table[i] += 1

table[6] = (table[6] + 1) // 2

print(max(table))