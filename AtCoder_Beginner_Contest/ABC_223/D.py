# import heapq
 
# N,M = map(int,input().split())
# G = []
# indegree = [0 for _ in range(N)] # 各ノードへの入次数を管理する。
 
# for _ in range(N):
#     G.append([])
 
# for _ in range(M):
#     A,B = map(int,input().split()) # AからBへ有向辺
#     G[A-1].append(B-1)
#     indegree[B-1] += 1
 
# heap = [] # 入次数が0のノードを保存する。辞書順で一番最初のものを出力する必要があり,idxの小さいものから取得する必要があるため、heapで管理
 
# for node in range(N):
#     if indegree[node] == 0:
#         heapq.heappush(heap, node)
 
# visited = [False for _ in range(N)]
 
# ans = [] 
 
 
# while len(heap) > 0:
#     cur_node = heapq.heappop(heap)
 
#     # if visited[cur_node]:#ノードを再訪している場合は、閉路が存在してしまっているため、
#     #     break
#     ans.append(cur_node)
#     # visited[cur_node] = True
#     for node_next_to in G[cur_node]:
#         indegree[node_next_to] -= 1
#         if indegree[node_next_to] == 0:
#             heapq.heappush(heap, node_next_to)
 
# if len(ans) != N:
#     print(-1)
#     exit(0)
 
# for i in range(N):
#     print(ans[i]+1,end=" ")



# import heapq

# N, M = map(int, input().split())
# route = [[] for _ in range(N+1)]
# in_deg = [0 for _ in range(N+1)]
# heap = []
# ans = []

# for _ in range(M):
#     a, b = map(int, input().split())
#     route[a].append(b)
#     in_deg[b] += 1

# for i in range(1, len(in_deg)):
#     if in_deg[i] == 0:
#         heapq.heappush(heap, i)

# # print(route)
# # print(in_deg)
# # print(heap)

# while heap:
#     num = heapq.heappop(heap)
#     ans.append(num)
#     if route[num]:
#         for i in route[num]:
#             in_deg[i] -= 1
#             if in_deg[i] == 0:
#                 heapq.heappush(heap, i)

# if len(ans) == N:
#     print(*ans)
# else:
#     print('-1')
        








# 先に現れる数字の中で、最小のものから取っていく
# 入次数が０の数字の中で最小のものを選んでいく
# 入次数が０の数字からでている有向辺の行き先の入次数を１減らす。
import heapq

N, M = map(int, input().split())
destination = [[] for _ in range(N+1)]
in_degree = [0] * (N+1)
hq = []
ans = []

for _ in range(M):
    A, B = map(int, input().split())
    destination[A].append(B)
    in_degree[B] += 1

for v in range(1, N+1):
    if in_degree[v] == 0:
        heapq.heappush(hq, v)

while hq:
    min_num = heapq.heappop(hq)
    ans.append(min_num)
    for j in destination[min_num]:
        in_degree[j] -= 1
        if in_degree[j] == 0:
            heapq.heappush(hq, j)

if len(ans) == N:
    print(*ans)
else:
    print(-1)



