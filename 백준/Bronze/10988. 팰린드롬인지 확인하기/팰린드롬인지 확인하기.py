s = input()

if len(s)%2 == 1:
    [print(1) if s[:len(s)//2] == s[len(s)//2+1:][::-1] else print(0)]
else:
    [print(1) if s[:len(s)//2] == s[len(s)//2:][::-1] else print(0)]