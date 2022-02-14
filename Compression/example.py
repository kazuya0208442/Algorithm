# # 座標圧縮したい数列
# A = [8, 100, 33, 33, 33, 12, 6, 1211]

# # 集合型にすることで重複を除去し、
# # 小さい順にソートする
# B = sorted(set(A))

# # B の各要素が何番目の要素なのかを辞書型で管理する
# D = { v: i for i, v in enumerate(B) }

# # 答え
# print(list(map(lambda v: D[v], A)))




# practice

A = [8, 100, 33, 33, 33, 12, 6, 1211]

B = sorted(set(A))

dict = {v: i for i, v in enumerate(B)}

compression_list = list(map(lambda x: dict[x], A))

print(compression_list)