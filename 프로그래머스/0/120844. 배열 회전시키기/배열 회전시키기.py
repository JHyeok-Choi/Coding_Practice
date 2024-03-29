def solution(numbers, direction):
    answer = []
    if direction == "right":
        numbers.insert(0, numbers.pop())
    else:
        numbers.append(numbers.pop(0))
    
    return numbers