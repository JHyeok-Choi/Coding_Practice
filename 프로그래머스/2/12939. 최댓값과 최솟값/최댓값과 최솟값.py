def solution(s):
    answer = ''
    s = sorted(map(int, s.split()))
    
    return f"{s[0]} {s[-1]}"