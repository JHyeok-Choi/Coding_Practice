def solution(n):
    answer = [0, 0, 3, 0, 11] + [0] * (n - 4)
    
    for i in range(4, n + 1, 2):
        answer[i] = answer[i - 2] * 3 + sum([answer[i] for i in range(i - 4, -1, -2)]) * 2 + 2
        
    return answer[n] % 1000000007