import sys
inp = sys.stdin.readline

N = int(inp())
table = [inp().rstrip() for _ in range(N)]

for i, j in enumerate(table):
    if '*' in j:
        heart = [i + 2 , j.index('*') + 1]
        break

left_arm = table[heart[0] - 1][: heart[1] - 1].count('*')
right_arm = table[heart[0] - 1][heart[1]:].count('*')
waist = [i[heart[1] - 1] for i in table].count('*') - 2
left_leg = [i[heart[1] - 2] for i in table[heart[0]:]].count('*')
right_leg = [i[heart[1]] for i in table[heart[0]:]].count('*')

print(*heart)
print(left_arm, right_arm, waist, left_leg, right_leg)