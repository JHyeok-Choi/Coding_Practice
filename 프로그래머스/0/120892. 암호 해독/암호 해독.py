def solution(cipher, code):
    answer = ''
    for i, j in enumerate(cipher):
        if i % code == code - 1:
            answer += j
    return answer