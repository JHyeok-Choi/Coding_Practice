N = int(input())

board = '012'

def sam(number):
    x, y = divmod(number, 3)
    if x == 0:
        return board[y]
    else:
        return sam(x) + board[y]

if str(sam(N)).count('2') or N == 0:
    print('NO')
else:
    print('YES')