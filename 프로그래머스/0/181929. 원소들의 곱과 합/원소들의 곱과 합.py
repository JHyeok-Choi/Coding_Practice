def solution(num_list):
    answer = 0
    gob = 1
    hap = 0
    
    for i in num_list:
        gob *= i
    for i in num_list:
        hap += i
    
    if gob < hap ** 2:
        answer = 1
    else:
        answer = 0
    
    return answer