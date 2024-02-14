import itertools

while True:
    table = list(map(int, input().split()))

    k = table[0]
    S = table[1:]

    for i in list(itertools.combinations(S, 6)):
        print(*i)

    if k == 0:
        exit()
        
    print('')