# BFS で解くぜ

# from collections import deque

# H, W = map(int, input().split())
# maze = [list(input()) for _ in range(H)]
# count = [[-1]*W for _ in range(H)]
# que = deque()
# ans = 1

# que.append([0, 0])
# count[0][0] = 1

# while que:
#     y, x = que.popleft()

#     for next_y, next_x in [[y+1, x], [y, x+1]]:
#         if next_y < H and next_x < W and maze[next_y][next_x] == '.' and count[next_y][next_x] == -1:
#             que.append([next_y, next_x])
#             count[next_y][next_x] = count[y][x] + 1
#             ans = max(ans, count[next_y][next_x])

# print(ans)



# DP で解いてみる。最後からさかのぼる。
# DP[i][j] : [i,j]マスからスタートした時の最大移動距離を表す。ゴールが１で、スタートが７とかになる。
# DP[i][j] = max(DP[i+1][j], DP[i][j+1]) + 1
# 下か右からしか遷移してこない、そのうち、大きいほうをとればいいという意味。

# INF = float('inf')
# INF = 10 ** 18


# H, W = map(int, input().split())
# maze = [list(input()) for _ in range(H)]
# DP = [[0]*(W+1) for _ in range(H+1)]

# for i in range(H-1, -1, -1):
#     for j in range(W-1, -1, -1):
#         if maze[i][j] == '#':
#             continue
#         DP[i][j] = max(DP[i+1][j], DP[i][j+1]) + 1
        
# print(DP[0][0])
# print(DP)






# DPで解くよ。今度は初めから見ていく。0行0列に番兵を置く。一個行と列を増やす。
# DP[i][j] = max(DP[i-1][j], DP[i][j-1]) + 1

H, W = map(int, input().split())
maze = [list(input()) for _ in range(H)]
DP = [[0]*(W+1) for _ in range(H+1)]

DP[1][1] = 1
ans = 1

for i in range(1, H+1):
    for j in range(1, W+1):
        if i == 1 and j == 1:
            continue
        if maze[i-1][j-1] == '#':
            continue
        if DP[i-1][j] == 0 and DP[i][j-1] == 0:   # スタート位置は(1,1)なので、(1,1)からつながってないといけない。前にいた位置が両方0なら、未知が途切れているからout
            continue

        DP[i][j] = max(DP[i-1][j], DP[i][j-1]) + 1
    
    ans = max(ans, max(DP[i]))

print(ans)