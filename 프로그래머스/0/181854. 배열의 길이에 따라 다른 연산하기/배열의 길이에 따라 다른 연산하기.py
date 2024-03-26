def solution(arr, n):
    answer = []
    length = len(arr)
    
    if length % 2 == 1:
        for i, j in enumerate(arr):
            if i % 2 == 0:
                arr[i] += n
    else:
        for i, j in enumerate(arr):
            if i % 2 == 1:
                arr[i] += n
        
    return arr