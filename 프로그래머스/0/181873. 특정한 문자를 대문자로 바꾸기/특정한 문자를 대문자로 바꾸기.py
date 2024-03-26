def solution(my_string, alp):
    answer = ''
    for i, j in enumerate(my_string):
        if j == alp:
            answer += j.upper()
        else:
            answer += j
            
    return answer