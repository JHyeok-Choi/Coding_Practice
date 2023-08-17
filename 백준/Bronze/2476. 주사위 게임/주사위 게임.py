N = int(input())
reward = 0

for _ in range(N):
    x, y, z = map(int, input().split())
    
    if x == y == z:
        reward = max(reward, 10000 + x * 1000)
    elif x == y or x == z:
        reward = max(reward, 1000 + x * 100)
    elif y == z:
        reward = max(reward, 1000 + y * 100)
    else:
        reward = max(reward, 100 * max(x,y,z))

print(reward)