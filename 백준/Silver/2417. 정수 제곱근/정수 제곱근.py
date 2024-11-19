n = int(input())

x, y = 0, n

while x <= y:
    z = (x + y) // 2
    if z ** 2 < n:
        x = z + 1
    else:
        y = z - 1
        
print(x)