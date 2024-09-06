a, b, c = input(), input(), input()


if a.isnumeric():
    i = int(a) + 3
elif b.isnumeric():
    i = int(b) + 2
else:
    i = int(c) + 1

print('FizzBuzz' if i % 15 == 0 else 'Fizz' if i % 3 == 0 else 'Buzz' if i % 5 == 0 else i)