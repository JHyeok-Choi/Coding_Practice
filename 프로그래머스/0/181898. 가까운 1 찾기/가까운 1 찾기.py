def solution(arr, idx):
    answer = 0
    answer = arr[idx:]
    
    if 1 not in answer:
        answer = -1
    else:
        answer = arr.index(1,idx)
        
    
        
    return answer