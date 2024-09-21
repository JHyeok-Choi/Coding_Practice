n, *m = list(map(lambda x: sum(map(int, x.split('+'))), input().split('-')))
print(n - sum(m))