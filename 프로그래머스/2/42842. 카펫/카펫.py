import math

def solution(brown, yellow):
    answer = []
    
    # half Perimeter of Rectangle = (brown + 4) / 2 = w + h
    
    hPoR = (brown + 4) // 2
    wh = brown + yellow
        
    for i in range(3, hPoR):
        w = wh // i
        
        if i * w == wh and (i - 2) * (w - 2) == yellow:
            answer = [w, i]
            break
        
    return answer