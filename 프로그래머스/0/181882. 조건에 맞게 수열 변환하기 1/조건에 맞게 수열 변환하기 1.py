def solution(arr):
    answer = []
    for i in arr:
        if i >= 50 and i % 2 == 0:
            answer += [i // 2]
        elif 50 > i and i % 2 == 1:
            answer += [i * 2]
        else:
            answer += [i]
    return answer