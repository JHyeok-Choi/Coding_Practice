def solution(arr):
    tmp = 2
    
    for i in range(11):
        if tmp ** i >= len(arr):
            arr += [0] * (tmp ** i - len(arr))
            break
        
    return arr