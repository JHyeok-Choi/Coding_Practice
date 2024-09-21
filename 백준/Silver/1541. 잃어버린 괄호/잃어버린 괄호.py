table = list(map(lambda x: sum(map(int, x.split('+'))), input().split('-')))
print(table[0] - sum(table[1:]))