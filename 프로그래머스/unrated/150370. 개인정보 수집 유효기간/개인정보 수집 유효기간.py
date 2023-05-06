def solution(today, terms, privacies):
    def to_days(date):
        Y, M, D = map(int, date.split("."))
        return Y * 336 + M * 28 + D
    
    terms_d = {i[0]: int(i[2:]) * 28 for i in terms}
    
    answer = [i+1 for i, privacy in enumerate(privacies) if to_days(today) >= (to_days(privacy[:-2]) + terms_d[privacy[-1]])]
            
    return answer