filenames = [input() for i in range(int(input()))]
answer = [list(j)[0] if len(j) <= 1 else '?' for j in (set(map(lambda x:x[i], filenames)) for i in range(len(filenames[0])))]
print(''.join(answer))