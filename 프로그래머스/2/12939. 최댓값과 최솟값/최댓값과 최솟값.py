def solution(s):    
    return (lambda x: f"{x[0]} {x[-1]}")(sorted(map(int, s.split())))