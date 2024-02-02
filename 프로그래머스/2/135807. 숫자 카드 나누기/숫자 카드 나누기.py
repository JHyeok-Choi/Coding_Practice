from functools import reduce
from math import gcd

def solution(arrayA, arrayB):
    answer = []
    gcdA = reduce(gcd, arrayA)
    gcdB = reduce(gcd, arrayB)

    if all(i % gcdB for i in arrayA):
        answer.append(gcdB)
    if all(j % gcdA for j in arrayB):
        answer.append(gcdA)

    if answer:
        answer = max(answer)
    else:
        answer = 0
    
    return answer