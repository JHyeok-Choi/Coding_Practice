def solution(n):
    nb = format(n, 'b')
    answer = n
    
    while True:
        answer += 1
        ab = format(answer, 'b')
        if nb.count('1') == ab.count('1'):
            break
    
    return answer