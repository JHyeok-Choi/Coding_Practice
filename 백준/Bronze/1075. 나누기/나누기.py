N, F = input(), int(input())

result = int(N[:-2]) * 100
while result % F:
    result += 1

print(str(result)[-2:])