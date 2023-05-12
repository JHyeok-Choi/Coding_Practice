def solution(wallpaper):
    answer = []
    x, y = [], []
    for i, j in enumerate(wallpaper):
        for k, l in enumerate(j):
            if l == '#':
                x.append(i)
                y.append(k)
    
    
    answer = [min(x), min(y), max(x)+1, max(y)+1 ]
    return answer