def solution(elements):    
    loop = elements * 2
    
    return len(set(sum(loop[i: i + j]) for j in range(len(elements)) for i in range(len(elements))))