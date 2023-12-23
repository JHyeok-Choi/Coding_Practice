import sys

def password_check():
    while True:
        test_case = sys.stdin.readline().rstrip()
        if test_case == 'end':
            break
        
        vowel = ['a', 'e', 'i', 'o', 'u']
        vowel_chk = False

        for i in range(len(test_case)):
            if test_case[i] in vowel:
                vowel_chk = True
            if i > 0 and test_case[i] == test_case[i - 1] and test_case[i] != 'e' and test_case[i] != 'o':
                vowel_chk = False
                break
            if i > 1 and test_case[i] in vowel and test_case[i - 1] in vowel and test_case[i - 2] in vowel:
                vowel_chk = False
                break
            elif i > 1 and test_case[i] not in vowel and test_case[i - 1] not in vowel and test_case[i - 2] not in vowel:
                vowel_chk = False
                break
        
        if vowel_chk:
            print(f"<{test_case}> is acceptable.")
        else:
            print(f"<{test_case}> is not acceptable.")


password_check()