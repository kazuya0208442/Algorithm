import heapq

# ヒープの要素はタプルに出来ます。これは、追跡される主レコードとは別に (タスクの優先度のような) 比較値を指定するときに便利です:
# >>> h = []
# >>> heappush(h, (5, 'write code'))
# >>> heappush(h, (7, 'release product'))
# >>> heappush(h, (1, 'write spec'))
# >>> heappush(h, (3, 'create tests'))
# >>> heappop(h)
# (1, 'write spec')






def dijkstra(s):
    hq = [(0, s)]
    heapq.heapify(hq) # リストを優先度付きキューに変換
    cost = [float('inf')] * n # 行ったことのないところはinf
    cost[s] = 0 # 開始地点は0
    while hq:
        c, v = heapq.heappop(hq)
        if c > cost[v]: # コストが現在のコストよりも高ければスルー   # なぜこのステップが必要なのか全くわからん。これに引っかかるパターンは既に下の操作で排除されているのではないのか。
            continue
        for d, u in e[v]:
            tmp = d + cost[v]
            if tmp < cost[u]:
                cost[u] = tmp
                heapq.heappush(hq, (tmp, u))
    return cost

n,m = map(int,input().split())
e = [[] for _ in range(n)]
for _ in range(m):
    a,b,t = map(int,input().split())
    a,b = a-1, b-1
    e[a].append((t, b))
    e[b].append((t, a))
ans = float('inf')
for i in range(n):
    dist = dijkstra(i)
    ans = min(ans, max(dist))
print(ans)
# print(e)                  # [[(10, 1)], [(10, 0), (10, 2)], [(10, 1)]]
# in 3 2
#    1 2 10
#    2 3 10