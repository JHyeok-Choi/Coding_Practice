def solution(s):
    answer = 0
    equal = 0
    noteq = 0
    
    for i in s:
        if equal == noteq:
            answer += 1
            x = i
        if x == i:
            equal += 1
        else:
            noteq += 1
            
    return answer