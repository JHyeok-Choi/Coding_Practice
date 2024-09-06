import sys

i = [int(m) + (3 - n) for n, m in enumerate(sys.stdin.read().split()) if m.isnumeric()][0]
print('FizzBuzz' if i % 15 == 0 else 'Fizz' if i % 3 == 0 else 'Buzz' if i % 5 == 0 else i)