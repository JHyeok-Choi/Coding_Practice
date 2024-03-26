def solution(num_list):
    answer = ''
    table = ''
    for i in num_list:
        if i % 2 == 1:
            answer += str(i)
        else:
            table += str(i)
            
    answer = int(answer) + int(table)
    
    return answer