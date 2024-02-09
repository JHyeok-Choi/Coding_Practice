import sys
input = sys.stdin.readline

N, S = map(int, input().split())
sequence = list(map(int, input().split()))
start, end = 0, 0
num = 0
Nm = 100001

while True:
    if num >= S:
        num -= sequence[start]
        Nm = min(Nm, end - start)
        start += 1
    elif end == N:
        break
    else:
        num += sequence[end]
        end += 1

print(0 if Nm == 100001 else Nm) 