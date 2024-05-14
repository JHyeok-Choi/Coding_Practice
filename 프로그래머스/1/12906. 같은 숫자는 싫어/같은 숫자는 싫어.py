def solution(arr):
    answer = [arr[0]]
    tmp = arr[0]
    
    for i in arr:
        if i != tmp:
            tmp = i
            answer.append(i)
            
    return answer