from collections import Counter

def solution(clothes):
    answer = 1

    cloth_comb = Counter([j for i, j in clothes])
    for k in cloth_comb.values():
        answer *= (k + 1)
    
    return answer - 1