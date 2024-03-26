def solution(num_list):
    answer = num_list
    if num_list[-1] > num_list[-2]:
        answer += [num_list[-1] - num_list[-2]]
    else:
        answer += [num_list[-1] * 2]
        
    return answer