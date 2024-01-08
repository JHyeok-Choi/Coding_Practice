import math

def solution(brown, yellow):
    answer = []
    
    # half Perimeter of Rectangle = (brown + 4) / 2 = w + h
    
    hPoR = (brown + 4) // 2
    wh = brown + yellow
    
    def calcul_h(a):
        h = (brown + yellow) // a
        return h
        
    for i in range(3, hPoR):
        w = calcul_h(i)
        if i * w == wh and (i - 2) * (w - 2) == yellow:
            if calcul_h(i) < i:
                continue
            else:
                print(i)
                answer = [w, i]
                break
        
    return answer