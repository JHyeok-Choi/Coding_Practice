N = int(input())
 
table = []
for i in str(N):
    table.append(int(i))
    
table.sort(reverse=True)
 
for i in table:
    print(i, end='')