def solution(babbling):
    answer = 0
    words = ["aya", "ye", "woo", "ma"]
    
    for i in babbling:
        length = 0
        
        for j in words:
            if i.find(j) != -1:
                length += len(j)
        
        if len(i) == length:
            answer += 1

    return answer