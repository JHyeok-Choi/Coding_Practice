def solution(code):
    answer = ''
    mode = 0
    for i, j in enumerate(code):
        if j == "1":
            mode = 0 if mode else 1
        else:
            if i % 2 == mode:
                    answer += j
    
    return answer if answer else "EMPTY"
