import sys
inp = sys.stdin.readline

N, M, B = map(int, inp().split())
chunk = [list(map(int, inp().split())) for _ in range(N)]
count = sys.maxsize
height = 0

for i in range(257):
    max_h, min_h = 0, 0
    
    for j in range(N):
        for k in range(M):
            if chunk[j][k] >= i:
                max_h += chunk[j][k] - i
            else:
                min_h += i - chunk[j][k]
    if max_h + B >= min_h:
        if min_h + (max_h * 2) <= count:
            count = min_h + (max_h * 2)
            height = i

print(count, height)