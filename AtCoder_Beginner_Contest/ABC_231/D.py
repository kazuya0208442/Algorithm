# N, M = map(int, input().split())
# frends = [[] for _ in range(N+1)]

# for _ in range(M):
#     a, b = map(int, input().split())
#     frends[a].append(b)
#     frends[b].append(a)

# for i in range(1, N+1):
#     if len(frends[i]) > 2:
#         print('No')
#         exit()
#     frends[i].sort()

# f_set = set(tuple(i) for i in frends)

# if len(f_set) != N+1:
#     print('No')
# else:
#     print('Yes')






# union-find

from typing import Optional, Any
import sys
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
parents = [-1] * (N+1)
dict = {}

def root(x: int) -> int:
    if parents[x] == -1:
        return x
    else:
        parents[x] = root(parents[x])
        return parents[x]

def merge(x: int, y: int):
    x = root(x)
    y = root(y)

    if x == y:
        print('No')
        exit()

    parents[x] = y
    return

for _ in range(M):            # roopがないかのチェック
    A, B = map(int, input().split())
    merge(A, B)

    dict[A] = dict.get(A, 0) + 1
    dict[B] = dict.get(B, 0) + 1

if M == 0:
    print('Yes')
elif max(dict.values()) > 2:
    print('No')
else:
    print('Yes')









    





