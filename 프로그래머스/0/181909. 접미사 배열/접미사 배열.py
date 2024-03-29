def solution(my_string):
    answer = sorted([my_string[-i:] for i in range(1, len(my_string) + 1)])
    
    return answer