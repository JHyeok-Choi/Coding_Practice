N = int(input())
shirt = list(map(int, input().split()))
T, P = map(int, input().split())

print(sum([i // T + 1 if (i % T) else i // T for i in shirt]))
print(N // P, N % P)