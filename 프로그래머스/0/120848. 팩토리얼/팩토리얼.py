def solution(n):
    table = [0, 1, 2]
    i = 3
    while True:
        if table[-1] == n:
            return table.index(table[-1])
        elif table[-1] > n:
            return table.index(table[-2])
        else:
            table.append(table[-1] * i)
            i += 1