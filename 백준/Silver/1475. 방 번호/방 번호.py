N = map(int, input())
table = {i:0 for i in range(10)}

for i in N:
    if i == 6 or i == 9:
        if table[6] <= table[9]:
            table[6] += 1
        else:
            table[9] += 1
    else:
        table[i] += 1

print(max(table.values()))