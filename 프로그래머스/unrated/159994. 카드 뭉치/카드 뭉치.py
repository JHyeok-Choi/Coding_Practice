def solution(cards1, cards2, goal):
    answer = 'Yes'
    text = ''
    
    for i in goal:
        if cards1 != [] and i == cards1[0]:
            text += cards1.pop(0)
        elif cards2 != [] and i == cards2[0]:
            text += cards2.pop(0)
        else:
            return "No"
    return answer