a, b = input(), input()
a_l, b_l = len(a), len(b)
dp = [''] * b_l

for i in range(a_l):
    lcs = ''
    for j in range(b_l):
        if len(lcs) < len(dp[j]):
            lcs = dp[j]
        elif a[i] == b[j]:
            dp[j] = lcs + a[i]

print(len(sorted(dp, key=len)[-1]))
print(sorted(dp, key=len)[-1])