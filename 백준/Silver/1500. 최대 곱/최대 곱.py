S, K = map(int, input().split())
X = S // K
Y = S % K
result = 1

for i in range(K):
    if Y > 0:
        result *= X + 1
        Y -= 1
    else:
        result *= X

print(result)