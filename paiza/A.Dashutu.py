# # # Sの位置から上下に検索して、'.'がある位置のインデックスが一致すれば道がある。
# # from collections import defaultdict

# # def main():
# #     H, W = map(int, input().split())
# #     A = [input() for _ in range(H)]
# #     index = 0
# #     # print(A)                  # ['######', '#....#', '#.##.#', '#.#S.#', '#.####', '#.....', '######']


# #     for i in range(H):
# #         if 'S' in A[i]:
# #             index = i
# #             break
    
# #     def up(A, index, H, W):
# #         up = index
# #         for j in range(index, H-1):      # 上方向探索
# #             str_j = A[j]
# #             str_j_plus_one = A[j+1]
# #             if str_j == '.' * W:
# #                 return down

# #             for k in range(len(A[j])):
# #                 if str_j[k] == str_j_plus_one[k] == '.':
# #                     up = j + 1
# #                     break
# #             if up == j:
# #                 break
# #         return up
    
# #     def down(A, index, H, W):
# #         down = index
# #         for j in range(index, 0, -1):      # 下方向探索
# #             str_j = A[j]
# #             str_j_plus_one = A[j-1]
# #             if str_j == '.' * W:
# #                 return down

# #             for k in range(len(A[j])):
# #                 if str_j[k] == str_j_plus_one[k] == '.':
# #                     down = j - 1
# #                     break
# #             if down == j:
# #                 break
# #         return down

# #     down_up = (down(A, index, H, W), up(A, index, H, W))


# #     B = list(zip(*A))           # [('#', '#', '#', '#', '#', '#', '#'), ('#', '.', '.', '.', '.', '.', '#'), ('#', '.', '#', '#', '#', '.', '#'), ('#', '.', '#', 'S', '#', '.', '#'), ('#', '.', '.', '.', '#', '.', '#'), ('#', '#', '#', '#', '#', '.', '#')]

# #     for i in range(W):
# #         if 'S' in B[i]:
# #             index = i
# #             break
    
# #     right_left = (down(B, index, W, H), up(B, index, W, H))

# #     print(down_up)
# #     print(right_left)

# # main()
        



# def main():
#     H, W = map(int, input().split())
#     A = [input() for _ in range(H)]
#     x, y = 0, 0

#     for i in range(H):
#         string = A[i]
#         if i == 0 or i == H-1:
#             A[i] = '!' * W
#             for j in range(len(string)):
#                 if j == 0 or j == len(string) - 1:
#                     A[i][j] = '!'
#                 if string[j] == 'S':
#                     x, y = i, j
    

#     def solve(MAZE, x, y):
#         if MAZE[x][y] == GOAL:
#             return print('YES')
#         MAZE[x][y] = '#'
#         for (next_x, next_y) in [(x+1, y), (x, y+1), (x, y-1), (x-1, y)]:
#             if MAZE[next_x][next_y] == '#':
#                 continue
#             route=solve(MAZE, next_x, next_y)
#             if route:
#                 return route

#     solve(A, x, y)

# main()



from collections import deque

H, W = map(int, input().split())
maze = [list(input()) for _ in range(H)]
que = deque()
ok = False

for i in range(H):
    for j in range(W):
        if maze[i][j] == 'S':
            sy, sx = i, j
            ok = True
            break
    if ok:
        break

que.append([sy, sx])

while que:
    y, x = que.popleft()

    if y == H-1 or x == W-1 or y == 0 or x == 0:
        print('YES')
        break

    maze[y][x] = '#'
    
    for ny, nx in ([y+1, x], [y-1, x], [y, x+1], [y, x-1]):
        if maze[ny][nx] != '#' and 0 <= ny < H and 0 <= nx < W:
            que.append([ny, nx]) 

else:
    print('NO')