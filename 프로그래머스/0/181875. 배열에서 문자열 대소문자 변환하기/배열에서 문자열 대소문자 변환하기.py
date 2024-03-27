def solution(strArr):
    answer = []
    for i in range(len(strArr)):
        if i % 2 == 1:
            answer += [strArr[i].upper()]
        else:
            answer += [strArr[i].lower()]
            
    return answer