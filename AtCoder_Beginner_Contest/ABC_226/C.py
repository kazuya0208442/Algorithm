

# # N = int(input())
# # A = [list(map(int, input().split())) for _ in range(N)]
# # ans = 0


# # # 5
# # # 1000000000 0
# # # 1000000000 1 1
# # # 1000000000 0
# # # 1000000000 1 3
# # # 1000000000 2 2 4




# # # for i in range(A[-1][1]):
# # #     num = A[-1][i+2] - 1
# # #     if A[num][1] == 0:
# # #         ans += A[num][0]
# # #     else:
        
# # def main(N, ans):
# #     num = A[N][1]
# #     if num == 0:
# #         ans += A[N][0]
# #         # print(ans)
# #         return ans 
# #     for i in range(num):
# #         # print(ans)
# #         n = A[N][i+2]-1
# #         ans = main(n, ans)
# #     ans += A[N][0]
# #     return ans

# # print(main(N-1, ans))
    

# N = int(input())
# X = [list(map(int ,input().split())) for _ in range(N)]

# T = [0]*(N+1)        # [0, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000]
# K = [0]*(N+1)        # [0, 0, 0, 0, 0, 4]
# A = [0]*(N+1)        # [0, [], [], [], [], [1, 2, 3, 4]]
# ans = 0

# for i in range(N):
#     x = X[i]
#     T[i+1] = x[0]
#     K[i+1] = x[1]
#     A[i+1] = x[2:]

# judge = [False] * (N+1)
# judge[N] = True

# for j in range(N, 0, -1):
#     if judge[j]:
#         for k in range(len(A[j])):
#             judge[A[j][k]] = True
#     else:
#         continue

# for k in range(N+1):
#     z = judge[k]
#     if z:
#         ans += T[k]

# print(ans)





# BFS DFS 印をつける　の３パターンでいこう
# BFSで攻める。queに入れて取り出して、時間を足して、必要な技を見て、queに入れる。
# {(b,6)}
# ->{(b,5),(c,6)}
# ->{(c,5),(c,5)}//ん？
# ->{(c,4),(d,5),(c,4),(d,5)}
# ->{(d,4),(d,4),(d,4),(d,4)}
# ->{(e,4),(d,3),(e,4),(d,3),(e,4),(d,3),(e,4),(d,3)}//あれ？
# このように指数的に増えていってしまうので、TLEしてしまいます。
# なぜこのようになるのかというと、
# ・(b,5)を見ているとき、(c,5)はまだ行ったことが無いのでqueに追加します
# ・(c,6)を見ているとき、(c,5)はまだ行ったことが無いのでqueに追加します
# という動作になってしまっているからです。

# これを解消するには、同じものを二回以上見ないように、「そこはもう調べることになっている」という段階で枝狩りしてやります。
# visitedに代入するタイミングを変えただけですね。


# 正しいBFS。フラグの場所に気を付けて。

# from collections import deque

# N = int(input())
# que = deque()
# needed_time = [0] * (N+1)
# needed_skill = [0] * (N+1)
# is_completed = [False] * (N+1)

# for i in range(1, N+1):
#     temp = list(map(int, input().split()))
#     time = temp[0]
#     skill = temp[2:]

#     needed_time[i] = time
#     needed_skill[i] = skill

# que.append(N)
# ans = 0
# is_completed[N] = True

# while que:
#     now = que.popleft()
#     ans += needed_time[now]
#     for next_num in needed_skill[now]:
#     # for next_num in sorted(needed_skill[now], reverse=True):
#         if not is_completed[next_num]:
#             is_completed[next_num] = True     # フラグのon/offは次の座標を調べたときに行う。
#             que.append(next_num)

# print(ans)
# print(needed_skill)
# print(needed_time)


# 5
# 10 0
# 10 1 1
# 10 2 1 2
# 10 1 1 
# 10 2 2 4



# フラグの場所を間違えてWAになるBFS

# from collections import deque

# N = int(input())
# que = deque()
# needed_time = [0] * (N+1)
# needed_skill = [0] * (N+1)
# is_completed = [False] * (N+1)

# for i in range(1, N+1):
#     temp = list(map(int, input().split()))
#     time = temp[0]
#     skill = temp[2:]

#     needed_time[i] = time
#     needed_skill[i] = skill

# que.append(N)
# ans = 0
# is_completed[N] = True

# while que:
#     now = que.popleft()
#     ans += needed_time[now]
#     is_completed[now] = True     # フラグのon/off
#     for next_num in needed_skill[now]:
#     # for next_num in sorted(needed_skill[now], reverse=True):
#         if not is_completed[next_num]:
#             que.append(next_num)

# print(ans)


# WAになるときの入力。40にならないといけないが、50になる。
# 5
# 10 0
# 10 1 1
# 10 2 1 2
# 10 1 1 
# 10 2 2 4





# 上から順番に、フラグのついたものの中身に、フラグを付けていく。
# DAGなので、最後から見ていけば、今見ているインデックスよりも小さい番号しか出てこない。


N = int(input())
time_needed = [0] * (N+1)
skill_needed = [0] * (N+1)
seen = [False] * (N+1)
seen[N] = True
ans = 0

for i in range(1, N+1):
    time, count, *skill = map(int, input().split())    # listを*で受け取れる。
    time_needed[i] = time
    skill_needed[i] = skill

for num in range(N, 0, -1):
    if seen[num]:
        for next_num in skill_needed[num]:
            if not seen[next_num]:
                seen[next_num] = True

for j in range(N+1):
    if seen[j]:
        ans += time_needed[j]

print(ans)





