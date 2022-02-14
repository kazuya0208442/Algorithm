# def main():
#     N = int(input())
#     grids = [list(map(int, input().split())) for _ in range(N)]
#     a_list = []
#     count = 0

#     for i in range(N):
#         for j in range(i+1, N):
#             if (grids[j][0] - grids[i][0]) != 0:
#                 a_list.append((grids[j][1] - grids[i][1]) / (grids[j][0] - grids[i][0]))
#         count = len(set(a_list))
#         a_list = []

#     return print(count)

# main()            # 大失敗。。。



# def main():
#     N = int(input())
#     grids = [list(map(int, input().split())) for _ in range(N)]   # [[3, 5], [5, 7], [9, 3]]
#     count = 0
#     # print(grids)

#     for i in range(N-2):
#         for j in range(i+1, N-1):
#             for k in range(j+1, N):    # 3つの点の組み合わせの求め方だよなこれ。
#                 xdif_ij = grids[i][0] - grids[j][0]
#                 ydif_ij = grids[i][1] - grids[j][1]

#                 xdif_jk = grids[j][0] - grids[k][0]
#                 ydif_jk = grids[j][1] - grids[k][1]

#                 # ydif_ij / xdif_ij != ydif_jk / xdif_jk:  # 両辺に xdif_ij * xdif_jk をかければ、0除算しなくていいのでは。

#                 if ydif_ij * xdif_jk != ydif_jk * xdif_ij:
#                     count += 1

#     return print(count)

# main()

# 外積ベクトル＝０というのは２つのベクトルのなす角度が０だね。|a×b| = |a||b|sinθ なので。


def is_triangle(a, b, c):      # [3,5], [4, 9], [9, 1]
    b1 = b[0] - a[0]
    b2 = b[1] - a[1]     # aから見たb
    c1 = c[0] - a[0]
    c2 = c[1] - a[1]     # aから見たc

    outer_product = b1 * c2 - b2 * c1
    # if outer_product != 0:
    #     return True
    return outer_product != 0


N = int(input())
grids = [list(map(int, input().split())) for _ in range(N)]
ans = 0

for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            if is_triangle(grids[i], grids[j], grids[k]):
                ans += 1

print(ans)