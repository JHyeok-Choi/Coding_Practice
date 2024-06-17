def solution(n):
    def trans(a, b):
        table = ''
        
        while a > 0:
            a, mod = divmod(a, b)
            table += str(mod)
            
        return table
    
    return int(trans(n, 3), 3)