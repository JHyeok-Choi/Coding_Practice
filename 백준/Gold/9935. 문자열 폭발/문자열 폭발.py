InpStr = input()
ExpStr = input()

stk = []

for i in InpStr:
    stk.append(i)
    if ''.join(stk[-len(ExpStr):]) == ExpStr:
        del stk[-len(ExpStr):]

print(''.join(stk) if ''.join(stk) != '' else 'FRULA')