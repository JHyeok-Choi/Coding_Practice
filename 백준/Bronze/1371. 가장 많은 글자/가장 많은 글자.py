import sys

text = sys.stdin.read()
table = [0] * 26

for i in text:
    if i.isalpha():
        table[ord(i) - 97] += 1

for idx, cnt in enumerate(table):
    if cnt == max(table):
        print(chr(97 + idx), end='')