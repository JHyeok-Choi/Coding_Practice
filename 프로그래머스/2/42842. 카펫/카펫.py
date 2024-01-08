import math

def solution(brown, yellow):
    answer = []
    
    # half Perimeter of Rectangle = (brown + 4) / 2 = w + h
    
    hPoR = (brown + 4) // 2
    wh = brown + yellow
        
    for h in range(3, hPoR):
        w = wh // h
        
        if w * h == wh and (w - 2) * (h - 2) == yellow:
            answer = [w, h]
            break
        
    return answer