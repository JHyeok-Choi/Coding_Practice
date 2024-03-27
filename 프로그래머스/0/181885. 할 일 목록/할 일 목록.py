def solution(todo_list, finished):
    answer = []
    for i,j in enumerate(todo_list):
        if finished[i]:
            pass
        else:
            answer += [j]
        
    return answer