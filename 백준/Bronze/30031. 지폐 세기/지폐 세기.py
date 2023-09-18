table = {136: 1000, 142: 5000, 148: 10000, 154:50000 }
count = 0

for _ in range(int(input())):
    A, _ = map(int, input().split())
    count += table[A]
print(count)