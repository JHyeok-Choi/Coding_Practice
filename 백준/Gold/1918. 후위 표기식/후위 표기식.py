infix= list(input())
table = []
postfix = ''

for i in infix:
    if i.isalpha():
        postfix += i
    elif i == '(':
        table += [i]
    elif i == '*' or i == '/':
        while table and (table[-1] == '*' or table[-1] == '/'):
            postfix += table.pop()
        table += [i]
    elif i == '+' or i == '-':
        while table and table[-1] != '(':
            postfix += table.pop()
        table += [i]
    else:
        while table and table[-1] != '(':
            postfix += table.pop()
        table.pop()

print(postfix + ''.join(reversed(table)))