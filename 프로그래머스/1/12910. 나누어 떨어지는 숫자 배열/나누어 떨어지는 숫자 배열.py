def solution(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor:
            pass
        else:
            answer += [i]
    
    if answer == []:
        answer = [-1]
    
    answer.sort()
    
    return answer