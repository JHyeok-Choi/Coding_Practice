def solution(name, yearning, photo):
    answer = []
    count = 0
    for i in photo:
        for j in i:
            if j in name:
                count += yearning[name.index(j)]
        answer.append(count)
        count = 0
    return answer