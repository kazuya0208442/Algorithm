import sys

def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    # Edit and remove this code as you like.
    print(lines)
    S = lines[0]
    Q = int(lines[1])
    t_k_str_list = []
    t_list = []
    k_list = []

    for row in lines[2:]:
        t, k = map(int, row.split())
        t_k_str_list.append([t,k])
        t_list.append(t)
        k_list.append(k)

    print(S, type(S), Q)
    print(t_k_str_list)
    print(t_list)
    print(k_list)
    # print(t_k_int_list)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)     


# 入力
# ABC
# 4
# 0 1
# 1 1
# 1 3
# 1 6
