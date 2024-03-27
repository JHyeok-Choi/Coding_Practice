def solution(n_str):
    answer = ''
    for i, j in enumerate(n_str):
        if j != "0":
            break
            
    answer = n_str[i:]
    
    return answer