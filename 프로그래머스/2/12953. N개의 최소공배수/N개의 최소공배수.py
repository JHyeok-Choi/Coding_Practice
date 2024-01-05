from math import gcd

def solution(arr):
    while len(arr) > 1:
        x = arr.pop(0)
        y = arr.pop(0)
        arr.append((x * y) // gcd(x, y))
    return arr[0]