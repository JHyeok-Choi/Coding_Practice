N = int(input())
M = int(input())
S = input()
count, repeat, i = 0, 0, 0

text = 'IO' * N + 'I'  # PN string
tl = len(text)  # PN len

while i + tl <= M:
    if text == S[i:i+(tl)]:  # PN있으면 count + 1, i + 2가 되게
        count += 1           # i+1은 I 다음인 O 라서 볼 필요 없습니다. 
        i += 2
    else:
        i += 1

print(count)