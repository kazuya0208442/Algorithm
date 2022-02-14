# zipで転置して、sumが取れるのか、１行の時もうまくいくのか検証

# >>> a = [[1,2,3]]
# >>> list(zip(*a))
# [(1,), (2,), (3,)]
# >>> b = [[1,2,3],[3,4,5]]
# >>> list(zip(*b))
# [(1, 3), (2, 4), (3, 5)]
# >>> list(map(sum, list(zip(*b))))
# [4, 6, 8]
# >>> list(map(sum, list(zip(*a))))
# [1, 2, 3]




# bit全探索で行くぜ。先に、買うor買わない を決定する。 

# N, M, X = map(int, input().split())
# cost_level = [list(map(int, input().split())) for _ in range(N)]
# ans = float('inf')

# for bit in range(1<<N):
#     used_book = []
#     cost = 0
#     for i in range(N):
#         if (bit >> i) & 1:
#             used_book.append(cost_level[i][1:])
#             cost += cost_level[i][0]
#     level = list(map(sum, zip(*used_book)))
#     if len(level) >= 1 and min(level) >= X:
#         ans = min(ans, cost)

# if ans == float('inf'):
#     print(-1)
# else:    
#     print(ans)





# 深さ優先探索DFSで全探索してみる
# 探索の途中で、値を書き換えると、ずっとその値が使われ続けるので、やめた。
# list in listを持たせたかったが、append文を書くと、もう、どの再帰でも同じリストが使われてしまう。
# 使う本の番号だけ持っておいて、最後にlistを作る方針にしたらできた。

import sys
sys.setrecursionlimit(10**6)
from typing import List

N, M, X = map(int, input().split())
cost_N_books = []
contents = []
ans = float('inf')

for _ in range(N):
    c, *level = map(int, input().split())
    cost_N_books.append(c)
    contents.append(level)

def dfs(book_number: int, cost: int, used_book=[]):
    if book_number == N:
        used_book_level = []
        for used_num in used_book:
            used_book_level.append(contents[used_num])
        understanding = list(map(sum, zip(*used_book_level)))
        if (len(understanding) >= 1) and (min(understanding) >= X):
            global ans
            ans = min(ans, cost)
        return
    for i in range(2):
        if i:
            dfs(book_number+1, cost+cost_N_books[book_number], used_book+[book_number])
        else:
            dfs(book_number+1, cost, used_book)

dfs(0, 0)

if ans == float('inf'):
    print(-1)
else:
    print(ans)








