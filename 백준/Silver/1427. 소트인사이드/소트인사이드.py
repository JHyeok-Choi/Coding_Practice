N = int(input())

table = list(map(int, str(N)))
table.sort(reverse=True)

print(*table, sep='')