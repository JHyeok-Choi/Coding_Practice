def solution(s):
    table = []
    
    if s.count('(') != s.count(')'):
        return False
    elif s[-1] == '(':
        return False
    
    for i in s:
        if i == '(':
            table.append(i)
        else:
            if len(table) == 0:
                return False
            else:
                table.pop()
        
    return True