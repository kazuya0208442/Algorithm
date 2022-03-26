import sys
from typing import List
from collections import deque

def main(lines: List):
    H, W = map(int, lines[0].split())
    maze = [list(row) for row in lines[1:]]
    visited = [[False] * W for _ in range(H)]
    area_and_length = []

    for i in range(H):
        for j in range(W):
            if maze[i][j] == '.':
                visited[i][j] = True
            elif visited[i][j]:
                continue
            else:
                visited[i][j] = True
                que = deque()
                que.append([i, j])
                area = 0
                length = 0
                sea_position = []

                while que:
                    y, x = que.popleft()
                    area += 1

                    for next_y, next_x in [[y+1, x], [y-1, x], [y, x+1], [y, x-1]]:
                        if (0 <= next_y <= H-1) and (0 <= next_x <= W-1) and (maze[next_y][next_x] == '#') and (not visited[next_y][next_x]):
                            que.append([next_y, next_x])
                            visited[next_y][next_x] = True
                        elif (0 <= next_y <= H-1) and (0 <= next_x <= W-1) and maze[next_y][next_x] == '.':
                            sea_position.append((next_y, next_x))
                        elif (next_y < 0) or (next_y >= H) or (next_x < 0) or (next_x >= W):
                            sea_position.append((next_y, next_x))

                area_and_length.append([area, len(sea_position)])
    
    area_and_length.sort(key=lambda x: (x[0], x[1]), reverse=True)

    for area, length in area_and_length:
        print(area, length)
                









if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)