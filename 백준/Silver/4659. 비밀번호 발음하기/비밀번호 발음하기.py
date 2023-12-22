import sys

input = sys.stdin.readline

consonant = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
vowel = ['a', 'e', 'i', 'o', 'u']


while True:
    consonant_cnt = 0
    vowel_cnt = 0
    test_case = input().rstrip()

    if test_case == "end":
        break
    else:
        consonant_stk = 0
        vowel_stk = 0
        last = 'aa'

        for idx, alpha in enumerate(test_case):
            if alpha in consonant:
                consonant_cnt += 1
                consonant_stk += 1
                vowel_stk = 0
            else:
                vowel_cnt += 1
                vowel_stk += 1
                consonant_stk = 0
            
            if (consonant_stk or vowel_stk) >= 3:
                print(f"<{test_case}> is not acceptable.")
                break

            if last == alpha:
                if last == 'e' or last == 'o':
                    pass
                else:
                    print(f"<{test_case}> is not acceptable.")
                    break
            last = alpha
            if idx == len(test_case) - 1:
                if vowel_cnt == 0:
                    print(f"<{test_case}> is not acceptable.")
                else:
                    print(f"<{test_case}> is acceptable.")