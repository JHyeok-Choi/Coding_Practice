def solution(emergency):
    answer = []
    temp = list(reversed(sorted(emergency)))
    
    for i in emergency:
        answer.append(temp.index(i) + 1)
    
    return answer