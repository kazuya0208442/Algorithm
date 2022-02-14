# 座標圧縮
# コメントアウトを外すと、新たな圧縮後の行列を表示できる。

H, W, N = map(int, input().split())
matrix = []
row = []
column = []

for i in range(N):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    row.append(A)
    column.append(B)
    matrix.append([A,B,i+1])

row_compression = {v: i for i, v in enumerate(sorted(set(row)))}
column_compression = {v: i for i, v in enumerate(sorted(set(column)))}

# height = max(row_compression.values())
# width = max(column_compression.values())

# matrix_compression = [['*'] * (width+1) for _ in range(height+1)]

for row, column, num in matrix:
    row = row_compression[row]
    column = column_compression[column]
    print(row+1, column+1)

    # matrix_compression[row][column] = num



# for row in matrix_compression:      # 問題違ったけど、これで、圧縮した新しい行列が作れたよ
#     print(row)

# [1, '*', '*', '*', '*', '*', '*', '*', '*', '*']
# ['*', 2, '*', '*', '*', '*', '*', '*', '*', '*']
# ['*', '*', 3, '*', '*', '*', '*', '*', '*', '*']
# ['*', '*', '*', 4, '*', '*', '*', '*', '*', '*']
# ['*', '*', '*', '*', 5, '*', '*', '*', '*', '*']
# ['*', '*', '*', '*', '*', 6, '*', '*', '*', '*']
# ['*', '*', '*', '*', '*', '*', 7, '*', '*', '*']
# ['*', '*', '*', '*', '*', '*', '*', 8, '*', '*']
# ['*', '*', '*', '*', '*', '*', '*', '*', 9, '*']
# ['*', '*', '*', '*', '*', '*', '*', '*', '*', 10]









