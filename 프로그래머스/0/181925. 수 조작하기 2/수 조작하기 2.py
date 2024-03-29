def solution(numLog):
    answer = ''
    
    for i in range(1, len(numLog)):
        result = 0
        result += numLog[i] - numLog[i - 1]
        
        if result == 1:
            answer += 'w'
        elif result == -1:
            answer += 's'
        elif result == 10:
            answer += 'd'
        elif result == -10:
            answer += 'a'
            
    return answer