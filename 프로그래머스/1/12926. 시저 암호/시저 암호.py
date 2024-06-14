def solution(s, n):
    answer = ''
    for i in s:
        code = ord(i)
        if i == ' ':
            answer += ' '
        elif (code <= 90 and 90 < code + n) or (96 < code and 122 < code + n):
            answer += chr(code + n - 26)
        else:
            answer += chr(code + n)
            
    
    return answer