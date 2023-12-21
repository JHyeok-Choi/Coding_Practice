import sys
input = sys.stdin.readline

N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

board.sort(key = lambda x : (x[1], x[2], x[3]), reverse=True)

index = [board[i][0] for i in range(N)].index(K)

for i in range(N):
    if board[index][1:] == board[i][1:]:
        print(i + 1)
        break