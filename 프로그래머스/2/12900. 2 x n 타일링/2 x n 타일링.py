def solution(n):
    answer = {0 : 0, 1 : 1, 2 : 2}
    for i in range(3, n + 1):
        answer[i] = ((answer[i - 1] + answer[i - 2]) % 1000000007)
    return answer[i]