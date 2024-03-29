def solution(my_string):
    answer = ''
    table = []
    for i in my_string:
        table.append(i.lower())
    table.sort()
    
    return ''.join(table)