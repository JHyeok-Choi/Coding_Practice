def solution(age):
    answer = ''
    table = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    for i in str(age):
        answer += table[int(i)]
    
    return answer