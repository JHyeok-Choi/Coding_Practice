from collections import Counter

def solution(k, tangerine):
    answer = 0
    
    for i in Counter(tangerine).most_common():
        if k > 0:
            k -= i[1]
            answer += 1
        
    return answer