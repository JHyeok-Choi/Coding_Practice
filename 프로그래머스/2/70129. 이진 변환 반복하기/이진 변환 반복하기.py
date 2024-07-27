def solution(s):
    x,y = 0, 0
    
    while s != "1":
        x, y, s = x + 1, y + s.count('0'), bin(s.count('1'))[2:]
    
    return [x, y]
