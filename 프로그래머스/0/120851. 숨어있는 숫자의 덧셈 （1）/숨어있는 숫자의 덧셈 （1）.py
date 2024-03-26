def solution(my_string):
    answer = [0 if i.isalpha() else int(i) for i in my_string ]
    return sum(answer)