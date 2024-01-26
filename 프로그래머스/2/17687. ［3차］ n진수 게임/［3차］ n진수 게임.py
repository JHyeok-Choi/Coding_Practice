def solution(n, t, m, p):
    answer = ''
    string = '0'
    table = [str(i) if i < 10 else chr(55 + i) for i in range(16)]
    
    for i in range(t * m):
        line = ''
        
        while i > 0:
            line = table[i % n] + line
            i //= n
        
        string += line
        
    for i in range(p - 1, t * m, m):
        answer += string[i]
        
    return answer