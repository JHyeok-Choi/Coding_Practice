from math import ceil

def solution(progresses, speeds):
    answer = []
    days = [ceil((100 - p )/ s) for p, s in zip(progresses, speeds)]
    count = 0
    current = days[0]
    
    for i in range(len(progresses)):
        if current < days[i]:
            answer.append(count)
            current = days[i]
            count = 0
        
        count += 1

    answer.append(count)
    
    return answer
