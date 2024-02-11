import itertools

N = int(input())
NM = [i for i in range(1, N + 1)]
K = list(map(int, input().split()))

def factorial(x):
    if x <= 1:
        return 1
    else:
        return x * factorial(x - 1)
    
if K[0] == 1:
    table = []
    K1 = K[1]
    for i in range(N, 0, -1):
        facto_i = factorial(i - 1)
        lev = (K1 - 1) // (facto_i)
        table.append(NM[lev])
        del NM[lev]
        K1 -= facto_i * lev

    print(*table)

else:
    K2 = K[1:]
    K1 = 1
    for i in range(N, 0, -1):
        facto_i = factorial(i - 1)
        lev = NM.index(K2[N - i])
        del NM[lev]
        K1 += facto_i * lev
        
    print(K1)