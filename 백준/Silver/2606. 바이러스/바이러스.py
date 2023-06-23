import sys
from collections import deque
inp = sys.stdin.readline

n = int(inp())  # 컴퓨터의 수.
m = int(inp())  # 컴퓨터 쌍의 수.

graph = [[] for _ in range(n+1)]  # 그래프 틀.
infected = [0] * (n+1)  # 컴퓨터에 감염여부 체크.

for i in range(m):
    x, y = map(int, inp().split())
    graph[x] += [y]  # x에 y를
    graph[y] += [x]  # y에 x를 연결합니다.

infected[1] = 1  # 1번 컴퓨터에서 시작하니 체크.
Q = deque([1])

while Q:
    z = Q.popleft()
    for j in graph[z]:
        if infected[j] == 0:  # 감염되지 않았다면 감염된걸로 체크.
            Q.append(j)
            infected[j] = 1

print(sum(infected)-1)