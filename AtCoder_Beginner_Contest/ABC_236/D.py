# 16C2 * 14C2 * 12C2 * 10C2 * 8C2 * 6C2 * 4C2 * 1/8! = 8*15 * 7*13 * 6*11 * 5*9 * 4*7 * 3*5 * 2*3 / 8! = 15*13*11*9*7*5*3 = 2 * 10**6

# from collections import deque

# N = int(input())
# A = [list(map(int, input().split())) for _ in range(2*N-1)]
# que = deque()

# for i in range(len(A[0])):
#     que.append([1, i+2, A[0][i]])

# while que:
#     y, x, a = que.popleft()

#     for i in range(y, 2*N-1):
#         if i == x-2:
#             continue
#         for j in range(A[i]):
#             que.append([i+1, j+2, a^A[i][j]])



# 先頭から選んでいく
# 排他的論理和は初期値０にしていい。0^a = a
# 10101111011 ^ 00000000000 = 10101111011


import sys
sys.setrecursionlimit(10**6)
from typing import List

N = int(input())
A = [list(map(int, input().split())) for _ in range(2*N-1)]
ans = 0

def dfs(dancer, score): 

    if len(dancer) == 0:
        global ans                       # globalを付けると関数外の変数にアクセスできる。
        ans = max(ans, score)
        return

    first_dancer = dancer[0]
 
    for i in range(1, len(dancer)):     # a = [1,3,5,7,9] で、a[5] = error だけど、a[5:] = [] スライスすると、空のリストが返ってくる。
        second_dancer = dancer[i]

        dfs(dancer[1:i] + dancer[i+1:], score ^ A[first_dancer-1][second_dancer-first_dancer-1])

dfs([i+1 for i in range(2*N)], 0)
print(ans)

