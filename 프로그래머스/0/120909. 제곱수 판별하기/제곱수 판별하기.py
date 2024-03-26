def solution(n):
    answer = 1 if int(n ** (1/2)) == n ** (1/2) else 2
    print(n ** (1/2))
    return answer