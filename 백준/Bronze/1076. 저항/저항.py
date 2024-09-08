table = {'black': '0', 'brown': '1', 'red': '2', 'orange': '3', 'yellow': '4', 'green': '5', 'blue': '6', 'violet': '7', 'grey': '8', 'white': '9'}
answer = ''

for i in range(3):
    if i == 2:
        answer += '0' * int(table[input()])
    else:
        answer += table[input()]

print(int(answer))