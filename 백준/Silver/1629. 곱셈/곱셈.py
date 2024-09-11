print(pow(*map(int, input().split())))

# A, B, C = map(int, input().split())

# # A^B % C => (A^(B/2) * A^(B/2)) % C      (if B는 짝수)
# #         => (A^(B/2) * A^(B/2) * A) % C  (if B는 홀수)  

# def mul(A, B, C):
#     if B == 1:
#         return(A % C)
    
#     num = mul(A, B // 2, C)

#     if B % 2:
#         return (num ** 2 % C * A) % C
#     else:
#         return (num ** 2) % C

# print(mul(A, B, C))
