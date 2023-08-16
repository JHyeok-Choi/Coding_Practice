import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())
graph = list([] for _ in range(N+1))
cnt = 0

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [False] * (N+1)

def DFS(x):
    visited[x] = True
    
    for node in graph[x]:
        if not visited[node]:
            DFS(node)

for i in range(1, N+1):
    if not visited[i]:
        DFS(i)
        cnt += 1

print(cnt)