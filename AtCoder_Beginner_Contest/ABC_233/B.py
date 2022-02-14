# L, R = map(int, input().split())
# S = list(input())

# S[L-1:R] = reversed(S[L-1:R])

# print(''.join(S))





# stringのままいく + [::-1] これを使う

# L, R = map(int, input().split())
# S = input()

# re_S = S[L-1:R]

# スライスで反転
# re_S = re_S[::-1]

# reverse()  error stringはimmutableで更新不可なので、元のstringを直接書き換えるreverse()methodは使えない
# re_S = re_S.reverse()

# イテレータを文字列に直接変換することはできないので、reversed()を使う場合はイテレータをリスト（一文字ずつが要素として格納されたリスト）に変換してからjoin()で一つの文字列に連結する。
# re_S = list(reversed(re_S))
# re_S = ''.join(re_S)


# print(S[:L-1] + re_S + S[R:])






# list を使って解く

# L, R = map(int, input().split())
# S = list(input())

# これは全く反転しない。スライスするとだめなのかも
# S[L-1:R].reverse()

# S本体を書き換え。reversed()は要素を逆順に取り出すイテレータを返す。元のリストは変更されない非破壊的処理。
# S[L-1:R] = reversed(S[L-1:R])

# print(reversed(S[L-1:R]))     # <list_reverseiterator object at 0x7f7607576370>
# s = reversed(S[L-1:R])
# print(s)                        # <list_reverseiterator object at 0x7f7607576370>

# print(''.join(S))








# 文字の入れ替えで行く！！whileでleftがrightを超えるまでやる。

L, R = [v-1 for v in map(int, input().split())]
S = list(input())

while L < R:
    S[L], S[R] = S[R], S[L]
    L += 1
    R -= 1

print(''.join(S))
