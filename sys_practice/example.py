import sys
example_list = []

# data = sys.stdin.read()
# print(data)


# for s in sys.stdin:
#     example_list.append(s)

# print(example_list)        # ['aaa\n', 'sss\n', 'ddd\n', 'fff\n', 'gggg\n']

# for s in sys.stdin:
#     example_list.append(s.rstrip())

# print(example_list)        # ['sss', 'ddd', 'fff', 'gggh', 'hhh']

# for s in sys.stdin:
#     example_list.append(s.strip('\n'))

# print(example_list)        # ['sss', 'ddd', 'fff', 'gggh', 'hhh']



# sys.stdin.readlines() は、複数行入力を１つのリストにする。
# N, M, Q = s[0].split() のように割り当てると'\n'は入らないから安心
# '\n' は、直接文字列として出てこない。改行として出てくるから、rstrip()でのぞけばいい

# s = sys.stdin.readlines()    # ['2 3 4\n', '2 3\n', '4 5\n', '3 4\n']
# print(s)

# print(s[0].rstrip())

# print(s[0].split())

# N, M, Q = s[0].split()
# print(N, M, Q)

# N, M, Q = map(int, s[0].split())
# print(N, M, Q)


# sys.stdin を調べる

# for s in sys.stdin:
#     print(s.rstrip())

# 出力してみる
sys.stdout.write('text\n\ntext\n') 





# def main(lines):
#     # このコードは標準入力と標準出力を用いたサンプルコードです。
#     # このコードは好きなように編集・削除してもらって構いません。
#     # ---
#     # This is a sample code to use stdin and stdout.
#     # Edit and remove this code as you like.
#     for i, v in enumerate(lines):
#         print("line[{0}]: {1}".format(i, v))

# if __name__ == '__main__':
#     lines = []
#     for l in sys.stdin.readline():
#         lines.append(l.rstrip('\r\n'))
#     main(lines)     


# import sys

# for i, x in enumerate(sys.argv):
#     print(i, x)
#     print(sys.argv)       # ['/home/kazuya/python-coding/sys_practice/example.py', 'aaa', 'sss', 'ddd']

# 0 /home/kazuya/python-coding/sys_practice/example.py
# 1 aaa
# 2 sss
# 3 ddd

# sys.argvはリスト（list)
# 一つ目の要素にスクリプトファイルのパスが格納される



