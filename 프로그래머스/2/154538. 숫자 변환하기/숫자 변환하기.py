def solution(x, y, n):
    answer = [1000000] * (y + 1)
    answer[x] = 0

    for i in range(x, y + 1):
        if i + n <= y:
            answer[i + n] = min(answer[i + n], answer[i] + 1)
        if i * 2 <= y:
            answer[i * 2] = min(answer[i * 2], answer[i] + 1)
        if i * 3 <= y:
            answer[i * 3] = min(answer[i * 3] , answer[i] + 1)
    
    if answer[y] == 1000000:
        return -1

    return answer[y]