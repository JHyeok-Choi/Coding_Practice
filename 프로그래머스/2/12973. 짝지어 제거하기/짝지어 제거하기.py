def solution(s):
    table = []
    
    for i in s:
        if table == []:
            table.append(i)
        else:
            if table[-1] != i:
                table.append(i)
            else:
                table.pop()
    
    if table:
        return 0
        
    return 1