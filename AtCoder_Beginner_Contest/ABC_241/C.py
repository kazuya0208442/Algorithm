
from typing import List
N = int(input())
grid = [list(input()) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if grid[i][j] == '.':
            grid[i][j] = 0
        else:
            grid[i][j] = 1

def check_6_height_width(grid: List[List[str]]) -> bool:
    







