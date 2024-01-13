from math import log2

def binary(num):
    cnt = 0
    
    for i in range(int(log2(num)) + 1):
        x = num % (2 ** (i + 1))
        cnt += (num - x) // 2
        if x > 2 ** i:
            cnt += x - 2 ** i
    
    return cnt

A, B = map(int, input().split())

print(binary(B + 1) - binary(A))