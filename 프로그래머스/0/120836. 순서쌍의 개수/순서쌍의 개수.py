def solution(n):
    answer = []
    for i in range(1, n + 1):
        if n//i * i == n:
            answer += [(n//i, i)]
            
    return len(answer)