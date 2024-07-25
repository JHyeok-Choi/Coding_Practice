def solution(s):
    answer = []
    table = {}
    
    for i, j in enumerate(s):
        if j not in table:
            table[j] = i
            answer.append(-1)
        else:
            answer.append(i - table[j])
            table[j] = i
        
    return answer