def solution(elements):
    answer = 0
    
    loop = 2 * elements
    table = set()
    
    for i in range(len(elements)):
        for j in range(len(elements)):
            table.add(sum(loop[i : i + j]))
            
    answer = len(table)
    
    return answer