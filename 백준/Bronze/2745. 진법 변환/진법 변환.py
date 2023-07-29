N, B = input().split()
table = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
total = [table.index(j)*(int(B)**i) for i, j in enumerate(N[::-1])]
print(sum(total))