def solution(s):
    answer = 0
    x_num = 0
    y_num = 0
    x = s[0]
    
    for i, j in enumerate(s):
        if x == j:
            x_num += 1
        else:
            y_num += 1
        if x_num == y_num:
            answer += 1
            if i+1 != len(s):
                x = s[i+1]
        else:
            if i == len(s)-1:
                answer += 1
    #if x == s[-1]:
    #    answer += 1
            
    return answer