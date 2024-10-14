table = {0: 0, 1: 1}

def fib(n):
    if n not in table:
        if n % 2 == 0:
            table[n] = (fib(n // 2) * (fib(n // 2) + 2 * fib((n // 2) - 1))) % 1000000007
        else:
            table[n] = (fib(n // 2) ** 2 + fib((n // 2) + 1) ** 2) % 1000000007
    
    return table[n]

print(fib(int(input())))