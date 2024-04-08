def solution(num_list, n):
    answer = []
    test = []
    for i in range(1, len(num_list) + 1):
        test.append(num_list[i - 1])
        if i % n == 0:
            answer.append(test)
            test = []
            
    return answer