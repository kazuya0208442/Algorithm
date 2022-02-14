# heapq.heapify(list) が必要なのは、listに値が入っているとき
# 空のリストなら、いきなり、heapq.heappush(list, i) ってやっても大丈夫。そっから優先順位付きキューになるから。

import heapq

N, M = map(int, input().split())
time_destination = [[] for _ in range(N+1)]
ans = float('inf')

for _ in range(M):
    a, b, t = map(int, input().split())
    time_destination[a].append([t, b])
    time_destination[b].append([t, a])

def dijkstra(start: int) -> int:
    INF = float('inf')
    time = [INF] * (N+1)
    time[start] = 0
    hq = [(0, start)]
    heapq.heapify(hq)

    while hq:
        t_sum, position = heapq.heappop(hq)

        if t_sum > time[position]:
            continue

        for needed_time, destination in time_destination[position]:
            temp = t_sum + needed_time
            if time[destination] > temp:
                time[destination] = temp
                heapq.heappush(hq, (temp, destination))

    return max(time[1:])

for i in range(1, N+1):
    ans = min(ans, dijkstra(i))

print(ans)





