import sys
inp = sys.stdin.readline

N = int(inp())

for _ in range(N):
    lt, wt, le, we = map(int, inp().split())
    if (lt * wt) > (le * we):
        print("TelecomParisTech")
    elif (lt * wt) < (le * we):
        print("Eurecom")
    else:
        print("Tie")