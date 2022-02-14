# import itertools
# from typing import Pattern

# def main():
#     H, W = map(int, input().split())
#     A = [list(map(int, input().split())) for _ in range(H)]

#     pattern_list = list(itertools.product(range(W), repeat=W))
#     pattern_list_new = []
#     print(len(pattern_list))

#     for i in range(len(pattern_list)):
#         pattern = pattern_list[i]
#         for j in range(W-1):
#             if abs(pattern[j] - pattern[j+1]) != 1:
#                 break
#             else:
#                 continue
#         pattern_list_new.append(pattern)
#     print(len(pattern_list_new))

# main()


# [1, 0, 0], [1, 0, 1], [2, 0, 2], [1, 0, 3] = [num, row, column]

# H, W = map(int, input().split())
# board = [list(map(int, input().split())) for _ in range(H)]

# from collections import deque
# que = deque()

# for i in range(W):
#     que.append([board[0][i], 0, i])

# while que:
#     now = que.popleft()

#     if now[1] < H-1:
#         for i in range(now[2]-1, now[2]+2):
#             if 0 <= i <= 3:
#                 now_copy = now[:]
#                 now_copy[0] += board[now_copy[1]+1][i]
#                 now_copy[1] += 1
#                 now_copy[2] = i
#                 que.append(now_copy)
#     else:
#         # print(que)
#         print(max(que)[0])
#         break                           # TLEだわ




# DP[i][j] i行目のｊ列目の時の最大値
# DP[i][j] = max(DP[i-1][j-1], DP[i-1][j], DP[i-1][j+1])

H, W = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(H)]
DP = [[0] * W for _ in range(H)]

for i in range(H):
    for j in range(W):
        if i == 0:
            DP[i][j] = board[i][j]
            continue

        DP[i][j] = DP[i-1][j] + board[i][j]
        if j-1 >= 0:
            DP[i][j] = max(DP[i][j], DP[i-1][j-1] + board[i][j])
        if j+1 < W:
            DP[i][j] = max(DP[i][j], DP[i-1][j+1] + board[i][j])


# print(DP)
print(max(DP[H-1]))