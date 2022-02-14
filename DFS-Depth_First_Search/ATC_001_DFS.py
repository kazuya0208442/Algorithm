# import sys
# sys.setrecursionlimit(10**7) # 再起回数の設定
 
# H, W = map(int, input().split())
# maze = [list(input()) for h in range(H)]
 
# for h in range(H):
#     for w in range(W):
#         if maze[h][w] == "s":
#             sx, sy = h, w
#             flg = True
#             break
#     if flg:
#         break
 
# # 深さ優先探索
# def dfs(x, y):
#     # 範囲外や壁の場合は終了
#     if y >= W or y < 0 or x >= H or x < 0 or maze[x][y] == '#':
#         return
 
#     # ゴールに辿り着ければ終了
#     if maze[x][y] == 'g':
#         print('Yes')
#         exit()
 
#     maze[x][y] = '#' # 確認したルートは壁にしておく
 
#     # 上下左右への移動パターンで再起していく
#     dfs(x+1, y)
#     dfs(x-1, y)
#     dfs(x, y+1)
#     dfs(x, y-1)
 
# dfs(sx, sy) # スタート位置から深さ優先探索
# print('No')



# import sys
# sys.setrecursionlimit(10**7)

# H, W = map(int, input().split())
# maze = [list(input()) for _ in range(H)]
# flg = False

# for i in range(H):
#     for j in range(W):
#         if maze[i][j] == 's':
#             sy, sx = i, j
#             flg = True
#             break
#     if flg:
#         break


# def maze_solve(y, x):
#     if y < 0 or x < 0 or y >= H or x >= W or maze[y][x] == '#':
#         return
#     if maze[y][x] == 'g':
#         print('Yes')
#         sys.exit()
#     maze[y][x] = '#'
#     maze_solve(y+1, x)
#     maze_solve(y-1, x)
#     maze_solve(y, x+1)
#     maze_solve(y, x-1)

# maze_solve(sy, sx)
# print('No')                 # PyPyだとTLEとMLEだったけどpython3.8.2ならACした。





# 今いる位置(y,x)だけ入力する。
# ゴールになったら終わり。
# それ以外は探索可能なマスをdfs()に突っ込む。
# dfs()に突っ込む前に、範囲内であること、壁じゃないこと、seenがFalseであること、を確認して、すぐにseenをTrueにすればオッケー
# 再帰関数をスタートし忘れるミスが多い。


import sys
sys.setrecursionlimit(10**6)


H, W = map(int, input().split())
maze = [list(input()) for _ in range(H)]
seen = [[False]*(W) for _ in range(H)]

for i in range(H):
    for j in range(W):
        if maze[i][j] == 's':
            y, x = i, j
            seen[y][x] = True

def dfs(y: int, x: int):
    if maze[y][x] == 'g':
        print('Yes')
        exit()
    
    for y_new, x_new in [[y+1,x], [y-1,x], [y,x+1], [y,x-1]]:
        if (0 <= y_new < H) and (0 <= x_new < W) and (maze[y_new][x_new] != '#') and (not seen[y_new][x_new]):
            seen[y_new][x_new] = True
            dfs(y_new, x_new)

dfs(y, x)
print('No')














