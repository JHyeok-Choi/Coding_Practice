table = []
for i in range(5):
    a = int(input())
    if a in table:
        table.remove(a)
    else:
        table.append(a)

print(*table)