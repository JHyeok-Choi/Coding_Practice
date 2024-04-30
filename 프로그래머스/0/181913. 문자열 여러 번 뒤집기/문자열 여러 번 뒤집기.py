def solution(my_string, queries):
    answer = ''
    my_string = list(my_string)
    
    for i in queries:
        my_string[i[0]:i[1]+1] = my_string[i[0]:i[1]+1][::-1]
    
    return ''.join(my_string)