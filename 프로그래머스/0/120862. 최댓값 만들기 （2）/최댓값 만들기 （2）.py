def solution(numbers):
    answer = 0
    numbers.sort()
    plus = numbers[-1] * numbers[-2]
    minus = numbers[0] * numbers[1]
    
    if plus > minus:
        answer = plus
    else:
        answer = minus
        
    return answer