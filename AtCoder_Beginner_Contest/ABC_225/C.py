# def main():
#     N, M = map(int, input().split())
#     B_list = [list(map(int, input().split())) for _ in range(N)]

#     for i in range(N-1):
#         yoko_a = B_list[i]
#         for j in range(M):
#             if len(yoko_a) == 1:
#                 break
#             if len(yoko_a) != 1 and abs(yoko_a[j] - yoko_a[j+1]):
#                 continue
#             else:
#                 return print('No')
            
    #７で割った余りを出して連結して、'0123456'にはいっているか。それがどの列でも同じかどうか。調べるのありやな。


# def main():
#     N, M = map(int, input().split())
#     B_matrix = [list(map(int, input().split())) for _ in range(N)]
#     # A_sample = [[] for _ in range(10)]                     

#     # for i in range(10):
#     #     row = A_sample[i]
#     #     for j in range(7):
#     #         A_ij = 7 * i + j + 1     # i -> i+1, j -> j+1 にすればつじつまが合う。
#     #         row.append(A_ij)
#     # print(A_sample)               # A_sample はこんなよ。[[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14], [15, 16, 17, 18, 19, 20, 21], [22, 23, 24, 25, 26, 27, 28], [29, 30, 31, 32, 33, 34, 35], [36, 37, 38, 39, 40, 41, 42], [43, 44, 45, 46, 47, 48, 49], [50, 51, 52, 53, 54, 55, 56], [57, 58, 59, 60, 61, 62, 63], [64, 65, 66, 67, 68, 69, 70]]

#     # if N != 1:
#     #     for x in range(N-1):
#     #         for y in range(x+1, N):
#     #             if B_matrix[x] == B_matrix[y]:
#     #                 return print('No')
    


#     for i in range(N):
#         row = B_matrix[i]
#         for j in range(M):
#             row[j] %= 7
    
#     first_row = B_matrix[0]
#     first_row_str = list(map(str, first_row))
#     # print(first_row_str)
#     # print(''.join(first_row_str))

#     if B_matrix == [first_row for _ in range(N)] and ''.join(first_row_str) in '1234560':
#         print('Yes')
#     else:
#         print('No')
# main()                 # お手上げ問題だわ。


# [1, 2, 3, 4, 5, 6, 7]
# [8, 9, 10, 11, 12, 13, 14]
# [15, 16, 17, 18, 19, 20, 21]

# (1, 1), (1, 2), (2, 1) とかでも大丈夫かな。(1, 1)に関しては正解だけどforループに引っかからないので、あらかじめ、valid=Trueにして、ダメなやつをFalseにしておとしていこう。　

N, M = map(int, input().split())
B_matrix = [list(map(int, input().split())) for _ in range(N)]

valid = True              # 一旦、全てをTrueにして、条件に合わないものをFalseにする。

for i in range(N):
    for j in range(M):
        if j + 1 < M and B_matrix[i][j] + 1 != B_matrix[i][j+1]:
            valid = False
            break
        if i + 1 < N and  B_matrix[i][j] + 7 != B_matrix[i+1][j]:
            valid = False
            break
        if j != M - 1 and B_matrix[i][j] % 7 == 0:
            valid = False
            break

if valid == True:
    print('Yes')
else:
    print('No')


