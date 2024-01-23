def solution(s):
    answer = []
    s = s[2:-2].split('},{')
    s = [list(map(int, i.split(','))) for i in s]
    s.sort(key=len)
    
    for j in s:
        for k in j:
            if int(k) not in answer:
                answer.append(int(k))
                
    return answer