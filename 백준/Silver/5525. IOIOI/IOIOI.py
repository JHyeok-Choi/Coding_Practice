N = int(input())
M = int(input())
S = input()
count = 0

text = 'IO' * N + 'I'  # PN string
tl = len(text)  # PN len

for i in range(M-(tl) + 1):  # PN길이만큼씩 탐색
    if text == S[i:i+(tl)]:  # PN있으면 count + 1
        count += 1

print(count)