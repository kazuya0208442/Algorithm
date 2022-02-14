# import sys
# sys.setrecursionlimit(10**6)


# N, M = map(int, input().split())
# p = [-1] * (N+1)
# bar_cnt = [0] * (N+1)
# point_cnt = [1] * (N+1)
# ans = 1
# mod = 998244353

# def root(x):
#     if p[x] == -1:
#         return x
#     p[x] = root(p[x])
#     return p[x]

# def merge(x, y):
#     x = root(x)
#     y = root(y)
#     if x == y:
#         bar_cnt[x] += 1
#         return
#     if x > y:
#         x, y = y, x
#     p[x] = y
#     bar_cnt[y] += bar_cnt[x] + 1
#     point_cnt[y] += point_cnt[x]


# for _ in range(M):
#     u, v = map(int, input().split())
#     merge(u, v)

# parent = [index for index, x in enumerate(p) if x == -1]
# # print(parent[1:])

# for i in parent[1:]:
#     if bar_cnt[i] == point_cnt[i]:
#         ans *= 2
#         ans %= mod
#     else:
#         ans = 0       # 全ての頂点から、という条件なので、１つでもoutならout

# print(ans)



# # if ans == 1:
# #     print('0')
# # else:
# #     print(ans)






# どの頂点についても、その頂点から他の頂点に向かう辺がちょうど 1 本ずつ存在するような向き付けの方法
# 木構造だと、末端の頂点から出ていく辺がない場合がある。M(辺の数) = N-1(頂点の数-1)
# よって、サイクルがあるグラフであれば、条件を満たす。M(辺の数) = N(頂点の数)

# 連結成分がいくつもあるので、union-findで各連結成分について、M=Nなのかどうかを調べればいい。
# どの頂点についても、その頂点から他の頂点に向かう辺がちょうど 1 本ずつ存在するような向き付けの方法なので
# 1つでもN!=Mの連結成分が見つかるとoutである。

# 親の「辺の数」と「頂点の数」をlistで持っておけばいい

import sys
sys.setrecursionlimit(10**6)

mod = 998244353
N, M = map(int, input().split())
parents = [-1] * (N+1)
edges = [0] * (N+1)
vertex_sum = [1] * (N+1)
ans = 1

def root(x: int) -> int:
    if parents[x] == -1:
        return x
    parents[x] = root(parents[x])
    return parents[x]

def merge(x: int, y: int):
    x = root(x)
    y = root(y)
    if x == y:
        edges[x] += 1
    else:
        # if x > y:
        #     x, y = y, x
        parents[x] = y
        edges[y] += edges[x] + 1
        vertex_sum[y] += vertex_sum[x]

for _ in range(M):
    u, v = map(int, input().split())
    merge(u, v)

for i in range(1, N+1):
    if parents[i] == -1:
        if edges[i] == vertex_sum[i]:
            ans *= 2
            ans %= mod
        else:
            print(0)
            exit()

print(ans)
