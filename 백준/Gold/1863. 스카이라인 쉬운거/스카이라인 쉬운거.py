import sys
input = sys.stdin.readline

n = int(input())
count = 0
table = [0]
altitude = [list(map(int, input().split()))[1] for _ in range(n)] + [0]

for i in altitude:
    h = i
    while table[-1] > i:
        if table[-1] != h:
            count += 1
            h = table[-1]
        table.pop()
    table.append(i)

print(count)