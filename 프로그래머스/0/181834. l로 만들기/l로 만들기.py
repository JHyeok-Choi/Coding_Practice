def solution(myString):
    answer = ''
    for i, j in enumerate(myString):
        if ord(j) < ord("l"):
            answer += "l"
        else:
            answer += j
    
    return answer