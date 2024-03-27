def solution(num_list):
    answer = 0
    odd = 0
    even = 0
    
    for i, j in enumerate(num_list):
        if i % 2 == 1:
            odd += j
        else:
            even += j
            
    return odd if odd >= even else even