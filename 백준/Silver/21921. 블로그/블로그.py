import sys

input = sys.stdin.readline

N, X = map(int, input().split())
visitor = list(map(int, input().split()))

count = 1

if max(visitor) == 0:
    print("SAD")
else:
    top_visitor_number = sum(visitor[:X])
    visitor_number = top_visitor_number
    for i in range(X, N):
        visitor_number = visitor_number - visitor[i - X] + visitor[i]
        if top_visitor_number < visitor_number:
            top_visitor_number = visitor_number
            count = 1
        elif top_visitor_number == visitor_number:
            count += 1

    print(top_visitor_number)
    print(count)