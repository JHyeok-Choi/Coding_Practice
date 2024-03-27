def solution(myString, pat):
    answer = 0
    subString = ""
    
    for i in myString:
        if i == "A":
            subString += "B"
        else:
            subString += "A"
            
    if pat in subString:
        answer = 1
    else:
        answer = 0
        
    return answer