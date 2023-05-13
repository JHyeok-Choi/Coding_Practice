def solution(ingredient):
    answer = 0
    material = []
    for i in ingredient:
        material.append(i)
        if material[-4:] == [1, 2, 3, 1]:
            for _ in range(4):
                material.pop()
            answer += 1
        
    return answer