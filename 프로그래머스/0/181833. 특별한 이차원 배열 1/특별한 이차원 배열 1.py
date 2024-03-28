def solution(n):
    answer = []
    
    for i in range(n):
        table = []
        for j in range(n):
            if i == j:
                table += [1]
            else:
                table += [0]
        answer.append(table)
        
    return answer