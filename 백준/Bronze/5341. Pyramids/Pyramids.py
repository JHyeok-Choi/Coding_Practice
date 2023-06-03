n = int(input())

def total(n):
    if n == 0:
        return 0
    else:
        return n + total(n-1)

while n:
    print(total(n))
    n = int(input())