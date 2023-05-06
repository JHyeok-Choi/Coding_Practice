def solution(today, terms, privacies):
    answer = []
    terms_d = {}
    Y, M, D = map(int, today.split('.'))
    total_t = Y*336 + M * 28 + D
    for term in terms:
        cate_t, month = term.split()
        terms_d[cate_t] = int(month) * 28
    
    for i, j in enumerate(privacies):
        date, cate_p = j.split()
        y, m, d = map(int, date.split('.'))
        total_p = y * 336 + m * 28 + d + terms_d[cate_p]
        if total_t >= total_p:
            answer.append(i+1)
            
    return answer