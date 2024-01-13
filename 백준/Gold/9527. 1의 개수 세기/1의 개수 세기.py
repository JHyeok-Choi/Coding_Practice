import sys
from collections import deque
input = sys.stdin.readline

def binary(num):
    if num < 2:
        return num
    
    dq = deque()
    num_a = num
    
    while num_a > 0:
        dq.append(num_a % 2)
        num_a //= 2
    
    cnt = len(dq) - 1
    
    return 2 ** (cnt - 1) * cnt + 1 + (num - 2 ** cnt) + binary(num - 2 ** cnt)

A, B = map(int, input().split())

print(binary(B) - binary(A - 1))