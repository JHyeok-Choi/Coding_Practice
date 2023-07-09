import sys
inp = sys.stdin.readline

T = int(inp())
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def scan(x,y):
    queue = [(x,y)]
    table[x][y] = 0

    while queue:
        x,y = queue.pop(0)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= M or ny < 0 or ny < 0  or ny >= N:
                continue

            if table[nx][ny] == 1:
                queue.append((nx,ny))
                table[nx][ny] = 0

for _ in range(T):
    M, N, K = map(int, inp().split())
    table = [[0] * N for _ in range(M)]
    cnt = 0

    for _ in range(K):
        X, Y = map(int, inp().split())
        table[X][Y] = 1
    
    for m in range(M):
        for n in range(N):
            if table[m][n] == 1:
                scan(m,n)
                cnt += 1

    print(cnt)