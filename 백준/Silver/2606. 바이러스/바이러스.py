import sys
inp = sys.stdin.readline

n = int(inp())
m = int(inp())

graph = [[] for i in range(n+1)]
wait = [1]
count = set()

for i in range(m):
    x, y = map(int, inp().split())
    graph[x] += [y]
    graph[y] += [x]

while wait:
    a = wait.pop(0)
    for i in graph[a]:
        if i not in count:
            wait.append(i)
            count.add(i)

print(len(count)-1)