def solution(food):
    answer = ''
    for i, j in enumerate(food):
        if j == 1:
            pass
        if j // 2 != 0:
            for _ in range(j // 2):
                answer += str(i)
                
    return answer + '0' + answer[::-1]