# # 入力
# H, W = map(int, input().split())
# A = [list(map(int, input().split())) for _ in range(H)]

# # 前処理
# yoko = list(map(sum, A))
# tate = list(map(sum, zip(*A)))

# # 各マス
# for i in range(H):
#     print(' '.join(map(lambda j: str(yoko[i] + tate[j] - A[i][j]), range(W)))   #模範解答だよ。

def main():
    H, W = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(H)]

    # print(matrix)                    # [[3, 4, 5], [9, 6, 4], [1, 2, 3]]
    # print(*matrix)                   # [3, 4, 5] [9, 6, 4] [1, 2, 3]  listの要素を1つ1つ取り出す。unpackできる。*でな。
    # print(zip(*matrix))              # <zip object at 0x7f166e60f240> 取り出した各listを１つずつzipに渡して、indexごとに組み合わせてtuppleを返す。
    # for i in zip(*matrix):           # (3, 9, 1) (4, 6, 2) (5, 4, 3)
    #     print(i)

    row_sum = list(map(sum, matrix))
    column_sum = list(map(sum, zip(*matrix)))
    # print(row_sum)
    # print(column_sum)

    # ans_matrix = [[0]*W for _ in range(H)]          # 0埋めの同じサイズの行列を作成。。。TLEがたくさん笑
    # print(ans_matrix)

    for i in range(H):
        for j in range(W):
            matrix[i][j] = row_sum[i] + column_sum[j] - matrix[i][j]
    
    # for k in range(H):
    #     print(*matrix[k])            # list oh list の unpackだとTLEになる。おそいんだねこれ。あれかな、generatorでその都度やった方が早いやつか。

    for k in range(H):                 # 数値を文字にして空白文字でくっつけるとACでした。mapの速さかな。generatorだっけ。
        print(" ".join(map(str, matrix[k])))

    # B_ij_list = []

    # for i in range(H):
    #     for j in range(W):
    #         B_ij = row_sum[i] + column_sum[j] - matrix[i][j]
    #         B_ij_list.append(B_ij)
    #     print(*B_ij_list)
    #     B_ij_list = []                # TLEが一つ出てしまい断念。。。惜しかったな。

    # for k in range(H):
    #     # print(B_ij_list)
    #     print(*B_ij_list[:W])
    #     B_ij_list = B_ij_list[W:]     # おおきな一つのlistに入れて、列の個数だけ切り取ってprintしたけどTLEになった。。。

main()