# s = input()
# s = s.replace('eraser', '')
# s = s.replace('erase', '')
# s = s.replace('dreamer', '')
# s = s.replace('dream', '')
# if s:
#   print('NO')
# else:
#   print('YES')       模範解答だよ。

def main():
    s = input()
    print(s)
    print(type(s))

    s = s.replace('eraser', '')
    s = s.replace('erase', '')
    s = s.replace('dreamer', '')
    s = s.replace('dream', '')

    if s:
        print('NO')
    else:
        print('YES')

main()
