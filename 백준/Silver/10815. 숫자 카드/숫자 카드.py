N = int(input())
Nlist = input().split()
M = int(input())
Mlist = input().split()
table = set(Nlist) & set(Mlist)

for i in Mlist:
    print('1' if i in table else '0', sep='\t')