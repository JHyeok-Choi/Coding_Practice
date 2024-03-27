def solution(myString):
    myString = myString.split("x")
    answer = [len(i) for i in myString]
    
    return answer