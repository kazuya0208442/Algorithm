# (A, B) = (N, N)  -N+1 <= k <= 0      A-N+1 <= A+k <= A ->  1 <= A+k <= N
# (A, B) = (1, 1)    0 <= k <= N-1     1 <= A+k <= N

# (Q-P+1) * (S-R+1)

# N, A, B = map(int, input().split())
# P, Q, R, S = map(int, input().split())

# min_1i = A + max(1-A, 1-B)
# max_1i = A + min(N-A, N-B)

# min_1j = B + max(1-A, 1-B)
# max_1j = B + min(N-A, N-B)

# min_2i = A + max(1-A, B-N)
# max_2i = A + min(N-A, B-1)

# min_2j = B - min(N-A, B-1)
# max_2j = B - max(1-A, B-N)

# # print(min(N-A, B-1))
# # print(max(1-A, B-N))


# for i in range(P, Q+1):
#     for j in range(R, S+1):
#         if (min_1i <= i <= max_1i) and i-A+B == j:
#             print('#', end='')
#             continue
#         if (min_2i <= i <= max_2i) and B+A-i == j:
#             print('#', end='')
#             continue
#         print('.', end='')
#     print()


        





# 再チャレンジ。(i,j)が白か黒かを判断できるように式変形してみた。kを消した。
# (i,j) i = A+k, j = B+k -> i-j = A-B
# (i,j) i = A+k, j = B-k -> i+j = A+B

N, A, B = map(int, input().split())
P, Q, R, S = map(int, input().split())

for i in range(P, Q+1):
    row = []
    for j in range(R, S+1):
        if (i-j == A-B) or (i+j == A+B):
            row.append('#')
        else:
            row.append('.')
    print(*row, sep='')

