T = int(input())
n_list = [0, 1, 2, 4]

for i in range(4, 12):
    n_list += [n_list[i-1] + n_list[i-2] + n_list[i-3]]

for _ in range(T):
    print(n_list[int(input())])