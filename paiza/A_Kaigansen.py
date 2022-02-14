from collections import deque

H, W = map(int, input().split())
mp = [list(input()) for _ in range(H)]
check = [[False] * W for _ in range(H)]
que = deque()
ans_list = []

for i in range(H):
    for j in range(W):
        if mp[i][j] == "#" and check[i][j] == False:
            que.append([i, j])
            check[i][j] = True
            scale = 0
            sea = list()
            while que:
                y, x = que.popleft()
                scale += 1
                for ny, nx in ([y+1, x], [y-1, x], [y, x+1], [y, x-1]):
                    if 0 <= ny < H and 0 <= nx < W and mp[ny][nx] == ".":
                        sea.append((ny, nx))
                    elif ny < 0 or nx < 0 or ny >= H or nx >= W:
                        sea.append((ny, nx))
                    elif 0 <= ny < H and 0 <= nx < W and mp[ny][nx] == "#" and check[ny][nx] == False:
                        que.append([ny, nx])
                        check[ny][nx] = True
            ans_list.append([scale, len(sea)])
        else:
            continue

ans = sorted(ans_list, key = lambda x: [x[0], x[1]], reverse=True)

for i in range(len(ans)):
    print(*ans[i])