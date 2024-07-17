N = int(input())
T = list(map(int, input().split()))
R = sum(T) + (len(T) - 1) * 8
print(R // 24, R % 24)