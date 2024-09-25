N = input()
table = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}

for i in N:
    if i == '6' or i == '9':
        if table['6'] <= table['9']:
            table['6'] += 1
        else:
            table['9'] += 1
    else:
        table[i] += 1

print(max(table.values()))