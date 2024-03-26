def solution(arr, k):
    answer = []
    if k % 2 == 1:
        for i in arr:
            answer += [i * k]
    else:
        for i in arr:
            answer += [i + k]
            
    return answer