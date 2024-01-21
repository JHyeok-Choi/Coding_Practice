a, b = input(), input()
a_l, b_l = len(a), len(b)
dp = [0] * b_l

for i in range(a_l):
    lcs = 0
    for j in range(b_l):
        if lcs < dp[j]:
            lcs = dp[j]
        elif a[i] == b[j]:
            dp[j] = lcs + 1

print(max(dp))