N = input()
table = [0] * 10
for i in N:
    if i == '6' or i == '9':
        if table[6] <= table[9]:
            table[6] += 1
        else:
            table[9] += 1
    else:
        table[int(i)] += 1

print(max(table))