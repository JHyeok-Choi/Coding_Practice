def solution(myString, pat):
    answer = 0
    pat = pat.lower()
    myString = myString.lower()
    if pat in myString:
        answer = 1
    else:
        answer = 0
        
    return answer