import sys
input = sys.stdin.readline

N = int(input())
password = input().rstrip()
asciia = 97
totalsec = 0

for alpha in password:
    N -= 1
    point = ord(alpha) - asciia

    if point > 0:
        totalsec += point * (26 ** (N + 1) - 26) // 25 + point

    totalsec += 1

print(totalsec)