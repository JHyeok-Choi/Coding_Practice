def solution(my_string):
    answer = []
    for i in range(26):
        answer += [my_string.count(chr(i + 65))]
    for j in range(26):
        answer += [my_string.count(chr(j + 97))]
        
    return answer