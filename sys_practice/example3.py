import sys

def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    # Edit and remove this code as you like.
    A, B, C, X = map(int, lines[0].split())      # lines[0].split() のように、インデックスを指定していつもの文字列にしてsplitするやつにもち込めればいいね。

    if X <= A:
        print(1)
    elif X <= B:
        print(C / (B - (A+1) + 1))
    else:
        print(0)

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)     

# ちゃんとACとれたよ！！！
# 手入力だと ctrl D 幼いといけないけど、提出すると行けた。