def solution(arr1, arr2):
    answer = []
    
    for i, j in zip(arr1, arr2):
        tmp = [i[k] + j[k] for k in range(len(i))]
        answer += [tmp]
        
    return answer