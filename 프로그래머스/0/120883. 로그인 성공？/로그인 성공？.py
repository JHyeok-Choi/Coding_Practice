def solution(id_pw, db):
    answer = 'fail'
    
    for i in db:
        if id_pw[0] == i[0]:
            if id_pw[1] == i[1]:
                return 'login'
            else:
                answer = 'wrong pw'
        
    return answer