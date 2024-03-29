def solution(my_string, m, c):
    answer = ''
    table = ''
    stk = []
    for i, j in enumerate(my_string, start=1):
        table += j
        if i  % m == 0:
            stk.append(table)
            table = ''
            
    for i in range(len(stk)):
        answer += stk[i][c - 1]

        
    return answer