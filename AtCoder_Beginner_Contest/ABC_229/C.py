# DP[i][j] i番目までを使って、jまで使った時の、重さの最小値
# DP[i][j] = min(DP[i-1][j], DP[i-1][j-w[i]] + v[i])

# N, W = map(int, input().split())
# B_max = 1000 * N + 1
# AB = [list(map(int, input().split())) for _ in range(N)]
# DP = [[0] * B_max for _ in range(N+1)]


# for i in range(1, N+1):
#     for j in range(1, B_max+1):
#         DP[i][j] = DP[i-1][j]
#         if j-AB[i-1][1] >= 0:
#             DP[i][j] = max(DP[i][j], DP[i-1][j] + j * AB[i-1][0])

# print(DP[3][:16])



# N, W = map(int, input().split())
# AB = [list(map(int, input().split())) for _ in range(N)]
# AB.sort(reverse=True)
# # print(AB)
# weight = 0
# v = 0


# for i in range(N):
#     while weight < W:
#         for j in range(AB[i][1]+1):
#             weight += 1
#             v += AB[i][0]
#     v -= AB[i][0]
#     print(v)
#     exit()
    



# N, W = map(int, input().split())
# AB = [list(map(int, input().split())) for _ in range(N)]
# AB.sort(reverse=True)
# weight = 0
# ans = 0

# for i in range(N):
#     if W-weight >= 1:
#         g = min(AB[i][1], W-weight)
#         ans += AB[i][0] * g
#         weight += g
#     else:
#         print(ans)
#         break

# else:
#     print(ans)








# 1gあたりのおいしさの大きいものから使っていく
# [美味しさ, 総量] で美味しさsortする。
# これは少し非効率、while文で一個ずつ足して確かめているから。
# minを使えばもっと早い。


# N, W = map(int, input().split())
# taste_weight = []
# sum = 0
# ans = 0

# for _ in range(N):
#     A, B = map(int, input().split())
#     taste_weight.append([A, B])

# taste_weight.sort(reverse=True)

# for i in range(N):
#     if sum + taste_weight[i][1] <= W:
#         ans += taste_weight[i][0] * taste_weight[i][1]
#         sum += taste_weight[i][1]
#     else:
#         while sum < W:
#             ans += taste_weight[i][0]
#             sum += 1
#         print(ans)
#         exit()

# print(ans)







# minを使えばもっと早い。