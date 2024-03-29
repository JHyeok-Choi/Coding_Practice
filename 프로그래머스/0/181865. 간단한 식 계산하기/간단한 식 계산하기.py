def solution(binomial):
    answer = 0
    splited = binomial.split()
    
    if splited[1] == '+':
        answer = int(splited[0]) + int(splited[2])
    elif splited[1] == '-':
        answer = int(splited[0]) - int(splited[2])
    else:
        answer = int(splited[0]) * int(splited[2])
        
    return answer