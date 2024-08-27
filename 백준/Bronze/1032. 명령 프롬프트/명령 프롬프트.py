answer = ''
filenames = [input() for i in range(int(input()))]

for j in (set(map(lambda x:x[i], filenames)) for i in range(len(filenames[0]))):
    if len(j) <= 1:
        answer += list(j)[0]
    else:
        answer += '?'

print(answer)