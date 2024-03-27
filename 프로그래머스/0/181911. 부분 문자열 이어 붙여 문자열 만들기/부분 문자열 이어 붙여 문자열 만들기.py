def solution(my_strings, parts):
    answer = ''
    for i, j in enumerate(my_strings):
        answer += j[parts[i][0]:parts[i][1] + 1]
    return answer