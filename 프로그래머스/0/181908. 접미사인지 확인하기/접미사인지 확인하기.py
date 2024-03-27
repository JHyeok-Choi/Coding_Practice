def solution(my_string, is_suffix):
    answer = 1 if my_string[my_string.rfind(is_suffix):] == is_suffix else 0
    return answer