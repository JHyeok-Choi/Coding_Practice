for _ in range(int(input())):
    n, q = input().split()
    print(q[:int(n)-1] + q[int(n):])