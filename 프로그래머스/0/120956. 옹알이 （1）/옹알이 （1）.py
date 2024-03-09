def solution(babbling):
    answer = 0
    words = ["aya", "ye", "woo", "ma"]
    
    for i in babbling:
        length = 0
        
        for j in words:
            i = i.replace(j, " ", 1)
        
        if i.strip() == "":
            answer += 1

    return answer