# 深さ優先探索(幅優先だと思うこれは)  コピーしたけど、popleftになってないからそこだけ修正した。最短距離になってなかった。

# from collections import deque

# INF = int(1e9)

# # 入力
# h, w = map(int,input().split())
# C = [] # 迷路の文字配列
# for i in range(h):
#     C.append(input())

# # スタート、ゴールの探索
# for y in range(h):
#     for x in range(w):
#         if C[y][x] == "s": # スタート座標はsx,sy
#             sx = x
#             sy = y
#         if C[y][x] == "g": # ゴール座標はgx,gy
#             gx = x
#             gy = y

# # 各座標への最短距離の配列（INFで初期化）
# D = [[INF] * w for i in range(h)]

# # 4方向の移動ベクトル
# dx = [1,0,-1,0]
# dy = [0,1,0,-1]

# # スタートからゴールへの最短距離を求める
# def dfs():
#     que = deque()
#     que.append([sy,sx]) # スタート地点をキューに入れる
#     D[sy][sx] = 0 # スタート地点の距離を0とする

#     # キューが空になるまで探索
#     while len(que) != 0:
#         p = que.pop() # 後入れのキューの要素を取り出す
#         if p[0] == gy and p[1] == gx: # ゴールなら探索終了
#             break
#         for i in range(4): # pから4方向に移動 移動後の点は(nx,ny)
#             ny = p[0] + dx[i]
#             nx = p[1] + dy[i]
#             # 移動可能か、訪れたことがあるかの判定
#             if 0 <= nx < w and 0 <= ny < h and C[ny][nx] != "#" and D[ny][nx] == INF:
#                 # 移動可能ならキューに入れて、その点の距離をpからの距離+1で確定する
#                 que.append([ny,nx])
#                 D[ny][nx] = D[p[0]][p[1]] + 1
#     return D[gy][gx]

# res = dfs()
# if res != INF:
#     print("Yes")
# else:
#     print("No")
# print(D)



# # 上の改良版、最短の歩数も記録。

# from collections import deque

# # 入力
# h, w = map(int,input().split())
# C = [] # 迷路の文字配列
# for i in range(h):
#     C.append(input())

# # スタート、ゴールの探索
# for y in range(h):
#     for x in range(w):
#         if C[y][x] == "s": # スタート座標はsx,sy
#             sx = x
#             sy = y
#         if C[y][x] == "g": # ゴール座標はgx,gy
#             gx = x
#             gy = y

# # 各座標への最短距離の配列（INFで初期化）
# D = [['%'] * w for i in range(h)]

# # 4方向の移動ベクトル
# dx = [1,0,-1,0]
# dy = [0,1,0,-1]

# # スタートからゴールへの最短距離を求める
# def dfs():
#     que = deque()
#     que.append([sy,sx]) # スタート地点をキューに入れる
#     D[sy][sx] = 0 # スタート地点の距離を0とする

#     # キューが空になるまで探索
#     while len(que) != 0:
#         p = que.popleft() # キューの要素を前から取り出す
#         if p[0] == gy and p[1] == gx: # ゴールなら探索終了
#             break
#         for i in range(4): # pから4方向に移動 移動後の点は(nx,ny)
#             ny = p[0] + dx[i]
#             nx = p[1] + dy[i]
#             # 移動可能か、訪れたことがあるかの判定
#             if 0 <= nx < w and 0 <= ny < h and C[ny][nx] != "#" and D[ny][nx] == '%':
#                 # 移動可能ならキューに入れて、その点の距離をpからの距離+1で確定する
#                 que.append([ny,nx])
#                 D[ny][nx] = D[p[0]][p[1]] + 1
#     return D[gy][gx]

# res = dfs()
# print(res)
# if res != '%':
#     print("Yes")
# else:
#     print("No")

# for i in range(h):
#     print(D[i])



# べた書きしたもの

# from collections import deque

# H ,W = map(int, input().split())
# maze = [list(input()) for _ in range(H)]
# count = [['#'] * W for _ in range(H)]

# for i in range(H):
#     for j in range(W):
#         if maze[i][j] == 's':
#             sy, sx = i, j
#         if maze[i][j] == 'g':
#             gy, gx = i, j

# que = deque()
# que.append([sy, sx])
# count[sy][sx] = 0

# while que:
#     y, x = que.popleft()
#     maze[y][x] = '#'

#     for ny, nx in [(y+1, x), (y-1, x), (y, x+1), (y, x-1)]:
#         if ny < 0 or nx < 0 or ny >= H or nx >= W or maze[ny][nx] == '#':
#             continue
#         count[ny][nx] = count[y][x] + 1
#         que.append([ny, nx])


# # for i in range(H):
# #     print(count[i])

# if count[gy][gx] == '#':
#     print('No')
# else:
#     print('Yes')






# from collections import deque

# H ,W = map(int, input().split())
# maze = [list(input()) for _ in range(H)]
# count = [['#'] * W for _ in range(H)]

# for i in range(H):
#     for j in range(W):
#         if maze[i][j] == 's':
#             sy, sx = i, j
#         if maze[i][j] == 'g':
#             gy, gx = i, j

# # que = deque()
# # que.append([sy, sx])
# # count[sy][sx] = 0

# def main():
#     que = deque()
#     que.append([sy, sx])
#     count[sy][sx] = 0

#     while que:
#         y, x = que.popleft()

#         if y == gy and x == gx:
#             break

#         for ny, nx in [(y+1, x), (y-1, x), (y, x+1), (y, x-1)]:
#             if ny < 0 or nx < 0 or ny >= H or nx >= W or maze[ny][nx] == '#' or count[ny][nx] != '#':
#                 continue
#             count[ny][nx] = count[y][x] + 1
#             que.append([ny, nx])
    
#     return count[gy][gx]

# ans = main()

# # for i in range(H):
# #     print(count[i])

# if ans == '#':
#     print('No')
# else:
#     print('Yes')



# 行った先を壁'#'にする作業をして、再度同じ道に行かないようにしたら、めっちゃ遅くなったから、やめた方がいいかも１０倍違う。
# 同じ大きさの二次元の配列を作ってアクセスするから遅くなるのかな。直接、mazeの方を変えたら早くなるかな。ゴールできるかどうかなら、来た道を壁にするだけでいいな。









from collections import deque    # 読み方はデック

H, W = map(int, input().split())
maze = [list(input()) for _ in range(H)]
seen = [[False]*(W) for _ in range(H)]
que = deque()

for i in range(H):
    for j in range(W):
        if maze[i][j] == 's':
            y, x = i, j
            seen[i][j] == True

que.append([y,x])

while que:
    y, x = que.popleft()
    if maze[y][x] == 'g':
        print('Yes')
        exit()
    
    for y_new, x_new in [[y+1,x], [y-1,x], [y,x+1], [y,x-1]]:
        if (0 <= y_new < H) and (0 <= x_new < W) and (maze[y_new][x_new] != '#') and (not seen[y_new][x_new]):
            que.append([y_new, x_new])
            seen[y_new][x_new] = True

print('No')