# DP[i][j] = max(DP[i-1][j-1], DP[i-1][j], DP[i-1][j+1]) + matrix[i][j]

import sys
from typing import List, Optional
from collections import deque

def main(lines: List):
    H, W = map(int, lines[0].split())
    matrix = [list(map(int, s.split())) for s in lines[1:]]
    DP = [[0] * W for _ in range(H)]
    DP[0] = matrix[0]

    for i in range(1, H):
        for j in range(W):
            DP[i][j] = DP[i-1][j] + matrix[i][j]
            if j-1 >= 0:
                DP[i][j] = max(DP[i][j], DP[i-1][j-1] + matrix[i][j])
            if j+1 <= W-1:
                DP[i][j] = max(DP[i][j], DP[i-1][j+1] + matrix[i][j])
    
    print(max(DP[H-1]))



if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)


