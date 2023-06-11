from collections import deque

def bfs(X):
    q = deque([X])  # N 값 할당.
    while q:
        X = q.popleft()  # 탐색할 값 할당.
        if X == K:  # 수빈이와 동생의 위치가 같을 때, 탐색시간 반환.
            return xboard[X]
        for nX in (X-1, X+1, 2 * X):  # 걷기, 순간이동 시 위치. 
            if 0 <= nX < MAX and not xboard[nX]:  # 이동할 위치가 가동범위 내, 간적 없는 위치일 때.
                xboard[nX] = xboard[X] + 1  # 탐색시간 추가.
                q.append(nX)  # 해당 위치 deque에 할당.

MAX = 100001  # 0부터 ~ 최대거리인 100000.
N, K = map(int, input().split())
xboard = [0] * MAX  # 최대치 만큼 list 미리 생성.

print(bfs(N))