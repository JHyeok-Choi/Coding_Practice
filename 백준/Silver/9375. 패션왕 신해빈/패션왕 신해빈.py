import sys
inp = sys.stdin.readline

for _ in range(int(inp())):
    dress = {}
    count = 1

    for _ in range(int(inp())):
        x, y = inp().split()
        if y not in dress:
            dress[y] = [x]
        else:
            dress[y].append(x)
    
    for i in dress:
        count *= (len(dress[i]) + 1)
    print(count - 1)