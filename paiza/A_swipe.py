

# N = int(input())
# game = [list(map(int, list(input()))) for _ in range(N)]
# seen = set()
# ans = 0

# for i in range(N):
#     for j in range(N-1):
#         if abs(game[i][j+1] - game[i][j]) == 1 and game[i][j+1] not in seen:
#             seen.add(game[i][j])
#             seen.add(game[i][j+1])
#         else:
#             ans = max(ans, len(seen))
#             seen = set()

# t_game = list(zip(*game))

# for i in range(N):
#     for j in range(N-1):
#         if abs(t_game[i][j+1] - t_game[i][j]) == 1 and t_game[i][j+1] not in seen:
#             seen.add(t_game[i][j])
#             seen.add(t_game[i][j+1])
#         else:
#             ans = max(ans, len(seen))
#             seen = set()

# temp_game = game[:]

# for i in range(N):
#     temp_game[i] = [0] * (N-1-i) + temp_game[i] + [0] * i

# left_top = list(zip(*temp_game))
# # print(left_top)

# for i in range(len(left_top)):
#     for j in range(len(temp_game)-1):
#         if abs(left_top[i][j+1] - left_top[i][j]) == 1 and left_top[i][j+1] not in seen:
#             seen.add(left_top[i][j])
#             seen.add(left_top[i][j+1])
#         else:
#             ans = max(ans, len(seen))
#             seen = set()

# print(ans)





from collections import deque
N = int(input())
game = [list(map(int, list(input()))) for _ in range(N)]
max_s = []

def main(row, column, matrix):
    que = deque()
    ans = 2

    for i in range(column):
        que.append([-1, matrix[0][i], 0, i, 2])

    while que:
        pre, now, y, x, count = que.popleft()
        ans = max(ans, count)

        if y+1 < row and matrix[y+1][x] != pre and abs(matrix[y+1][x] - now) == 1:
            que.append([now, matrix[y+1][x], y+1, x, count+1])
        
        if not que and y+1 < row:
            for i in range(column):
                que.append([matrix[y][i], matrix[y+1][i], y+1, i, 2])


    max_s.append(ans)


main(N, N, game)                # tate

t_game = list(zip(*game))
main(N, N, t_game)              # yoko


temp_game = game[:]
for i in range(N):
    temp_game[i] = [-1] * (N-1-i) + temp_game[i] + [-1] * i
# print(temp_game)
main(N, 2*N-1, temp_game)       # naname_left



temp_game = game[:]
for i in range(N):
    temp_game[i] = [-1] * i + temp_game[i] + [-1] * (N-1-i)

# print(temp_game)

main(N, 2*N-1, temp_game)       # naname_right

print(max(max_s))

