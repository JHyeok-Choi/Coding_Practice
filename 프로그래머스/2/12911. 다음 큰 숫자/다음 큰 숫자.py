def solution(n):
    nb = format(n, 'b')
    
    while True:
        n += 1
        ab = format(n, 'b')
        if nb.count('1') == ab.count('1'):
            break
    
    return n