import sys
from typing import List, Optional
from collections import deque

def main(lines: List):
    H, W = map(int, lines[0].split())
    maze = [list(s) for s in lines[1:]]
    que = deque()

    for i in range(H):
        for j in range(W):
            if maze[i][j] == 'S':
                y, x = i, j
    
    que.append([y, x])

    while que:
        y, x = que.popleft()
        if (y == 0) or (y == H-1) or (x == 0) or (x == W-1):
            print('YES')
            exit()

        for next_y, next_x in [[y+1, x], [y-1, x], [y, x+1], [y, x-1]]:
            if (0 <= next_y <= H-1) and (0 <= next_x <= W-1) and (maze[next_y][next_x] != '#'):
                que.append([next_y, next_x])
                maze[next_y][next_x] = '#'
    
    print('NO')
        
    


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)


