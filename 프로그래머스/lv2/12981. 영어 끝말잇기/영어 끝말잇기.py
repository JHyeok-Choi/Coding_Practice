def solution(n, words):
    answer = []
    
    for i, j in enumerate(words):
        if i > 0 and j[0] != words[i-1][-1]:
            answer.append(i % n + 1)
            answer.append(i // n + 1)
            break
        if j in words[:i]:
            answer.append(i % n + 1)
            answer.append(i // n + 1)
            break
    if answer == []:
        answer = [0, 0]

    return answer