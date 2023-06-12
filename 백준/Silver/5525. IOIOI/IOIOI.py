N = int(input())
M = int(input())
S = input()
count, repeat, i = 0, 0, 0

while i < M - 1:
    if S[i:i+3] == 'IOI':  # 현위치 문자가 'IOI' 일때
        count += 1
        i += 2             # i+1은 I 다음인 O 라서 볼 필요 없습니다. 
        if count == N:     # PN 일 떄
            repeat += 1
            count -= 1
    else:
        i += 1
        count = 0

print(repeat)
