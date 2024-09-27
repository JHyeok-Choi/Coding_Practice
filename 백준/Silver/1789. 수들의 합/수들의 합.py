S = int(input())
cnt = 0
tt = 0

while 1:
    cnt += 1
    tt += cnt
    if tt > S:
        break

print(cnt - 1)