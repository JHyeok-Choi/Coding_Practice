files = [input() for i in range(int(input()))]
print(''.join([list(j)[0] if len(j) <= 1 else '?' for j in (set(map(lambda x:x[i], files)) for i in range(len(files[0])))]))