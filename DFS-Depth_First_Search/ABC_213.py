# # 再帰回数上限。再帰関数を使うときは必ず最初に書くこと
# import sys
# sys.setrecursionlimit(10**6)

# # 入力の受け取り
# N=int(input())

# # 道の情報格納リスト
# connect=[[] for i in range(N+1)]

# # 道の情報受け取り
# for i in range(N-1):
#     A,B=map(int, input().split())
#     connect[A].append(B)
#     connect[B].append(A)
# # connect[2]=[1,4]ならば2と1,4がつながっている

# # 小さい順に回るからソート
# for i in range(N+1):
#     connect[i].sort()

# # 答えの格納用リスト
# ans=[]

# # DFS(今いる町,前にいた町)
# def DFS(now,pre):
#     # 今いる町を答えに入れる
#     ans.append(now)
#     # to=今いる町から行ける町
#     for to in connect[now]:
#         # もしtoが前にいた町と違うなら
#         if to!=pre:
#             # 更に先へ探索する
#             DFS(to,now)
#             # 戻ってきたら答えへ格納
#             ans.append(now)

# # 最初の町=1,前にいた町=-1(前にいた町がないので便宜上-1)としてスタート
# DFS(1,-1)

# # 答えの出力
# print(*ans)







# 潜った後に、すぐ、今の場所を記録すればオッケー
# 次に行けるところを記録して、戻ってきたタイミングで、現在地を記録してるみたいな。

import sys
sys.setrecursionlimit(10**6)

N = int(input())
edges = [[] for _ in range(N+1)]
visited = [False] * (N+1)
visited[1] = True
route = [1]

for _ in range(N-1):
    A, B = map(int, input().split())
    edges[A].append(B)
    edges[B].append(A)

for v in edges:
    v.sort()

def dfs(x: int):

    for to in edges[x]:
        if (not visited[to]):
            visited[to] = True
            route.append(to)
            dfs(to)
            route.append(x)
            
dfs(1)
print(*route)






