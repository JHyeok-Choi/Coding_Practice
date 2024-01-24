def solution(word):
    answer = 0
    table = ["A", "E", "I", "O", "U"]
    for idx, val in enumerate(word):
        rec = 0
        for j in range(0, 5 - idx):
            rec += (5 ** j)
        answer += rec * table.index(val) + 1
        
    return answer