def solution(t, p):
    answer = 0
    
    leng = len(p)
    for i in range(len(t) - leng + 1):
        if int(t[i: leng + i]) <= int(p):
            answer += 1

    return answer