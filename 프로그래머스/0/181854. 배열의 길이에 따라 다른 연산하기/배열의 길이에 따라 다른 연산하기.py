def solution(arr, n):
    answer = []
    length = len(arr)
    
    for i, j in enumerate(arr):
        if (length % 2 == 1 and i % 2 == 0) or (length % 2 == 0 and i % 2 == 1):
            arr[i] += n
        
    return arr
