N, M = map(int, input().split())

if 2 >= M:
    print('NEWBIE!')
elif N >= M:
    print('OLDBIE!')
else:
    print('TLE!')