def factorial(n):
    result = 1
    
    for i in range(1, n + 1):
        result *= i
        
    return result

def solution(n, k):
    answer = []
    table = [i for i in range(1, n + 1)]
    k -= 1
    
    for i in range(n, 0, -1):
        q, k = divmod(k, factorial(i - 1))
        answer.append(table.pop(q))
        
    return answer