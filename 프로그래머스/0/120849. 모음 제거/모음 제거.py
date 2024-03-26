def solution(my_string):
    answer = ''
    table = ["a", "e", "i", "o", "u"]
    for i in my_string:
        if i not in table:
            answer += i
    return answer