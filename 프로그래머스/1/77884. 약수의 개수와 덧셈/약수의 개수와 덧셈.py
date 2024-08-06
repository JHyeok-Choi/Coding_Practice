def solution(left, right):
    answer = 0
    
    def divisor(num):
        result = []
        for i in range(1, int(num ** (1 / 2)) + 1):
            if num % i == 0:
                result.append(i)
                if i < num // i:
                    result.append(num // i)
        
        return len(result)
    
    for j in range(left, right + 1):
        count = divisor(j)
        answer += -j if count % 2 else j
            
    
    return answer