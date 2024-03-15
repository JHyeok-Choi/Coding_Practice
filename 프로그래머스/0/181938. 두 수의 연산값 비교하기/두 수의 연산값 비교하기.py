def solution(a, b):
    answer = 0
    tmp1, tmp2 = int(str(a) + str(b)), 2 * a * b
    answer = tmp1 if tmp1 >= tmp2 else tmp2
    return answer