N = map(int, input())
table = {i:0 for i in range(10)}

for i in N:
    if i == 9:
        table[6] += 1
    else:
        table[i] += 1

table[6] = (table[6] + 1) // 2

print(max(table.values()))