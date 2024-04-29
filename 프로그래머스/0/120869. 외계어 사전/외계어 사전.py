def solution(spell, dic):
    answer = 0
    for i in dic:
        for j in spell:
            if j in i:
                answer += 1
        if answer == len(spell):
            return 1
        answer = 0
    return 2