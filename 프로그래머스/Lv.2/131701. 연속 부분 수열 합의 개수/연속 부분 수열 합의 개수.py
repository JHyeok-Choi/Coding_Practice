def solution(elements):    
    loop = 2 * elements
    table = set(sum(loop[i: i + j]) for j in range(len(elements)) for i in range(len(elements)))
    
    return len(table)
