

# N, W = map(int, input().split())
# w_v = [list(map(int, input().split())) for _ in range(N)]
# DP = [[0] * (W+1) for _ in range(N+1)]

# # DP[i][j] i番目のお菓子で重さがj以下になる選び方での価値の最大値
# # DP[i][j] = max(DP[i-1][j], DP[i-1][j-w[i]] + v[i])

# for i in range(1, N+1):
#     for j in range(W+1):
#         DP[i][j] = DP[i-1][j]
#         if j-w_v[i-1][0] >= 0:
#             DP[i][j] = max(DP[i][j], DP[i-1][j-w_v[i-1][0]] + w_v[i-1][1])

# # print(DP)
# print(DP[N][W])



# N ,W = map(int, input().split())
# dp = [0]*(W+1)
 
# for _ in range(0, N):
#     weight, value = map(int, input().split())
#     for w in range(W, weight-1, -1):
#         if dp[w-weight] + value > dp[w]:
#             dp[w] = dp[w-weight] + value
 
# print(dp[W])







# DP[i][j] = i個目までの商品を見て、重さがj以下になるように商品を買ったときの、価値の総和の最大値
# DP[i][j] = max(DP[i-1][j], DP[i-1][j-w(i)] + v(i))
# i個目の商品を選ぶ or 選ばない の二択

# 初期値が気になったけど、0個目があるとして、価値は０だから全部ゼロ。
# 1個目は、j-w(1) >= 0 を満たすjの時だけ選ばれる。
# 2個目は、j-w(2) >= 0 を満たすjの時に考慮される。
# もし、w(1) > w(2)で v(1) < v(2) なら、つまり、2個目の方が軽くて、価値も高いなら、
# j(1) > j(2) のように、jが小さいところから上書きが始まり、うーーｎ
# とりあえずこれでいける！！1個目が選ばれないパターンも考慮されている。

N, W = map(int, input().split())
weight = [0]
value = [0]
DP = [[0] * (W+1) for _ in range(N+1)]

for _ in range(N):
    w, v = map(int, input().split())
    weight.append(w)
    value.append(v)

for i in range(1, N+1):
    for j in range(W+1):
        DP[i][j] = DP[i-1][j]
        if j-weight[i] >= 0:
            DP[i][j] = max(DP[i][j], DP[i-1][j-weight[i]] + value[i])

print(DP[N][W])
print(weight)
print(value)
for row in DP:
    print(row)


# 6 15   # N,W
# 6 5
# 5 6
# 6 4
# 6 6
# 3 5
# 7 2

# 17     # DP[N][W]

# [0, 6, 5, 6, 6, 3, 7]
# [0, 5, 6, 4, 6, 5, 2]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
# [0, 0, 0, 0, 0, 6, 6, 6, 6, 6, 6, 11, 11, 11, 11, 11]
# [0, 0, 0, 0, 0, 6, 6, 6, 6, 6, 6, 11, 11, 11, 11, 11]
# [0, 0, 0, 0, 0, 6, 6, 6, 6, 6, 6, 12, 12, 12, 12, 12]
# [0, 0, 0, 5, 5, 6, 6, 6, 11, 11, 11, 12, 12, 12, 17, 17]
# [0, 0, 0, 5, 5, 6, 6, 6, 11, 11, 11, 12, 12, 12, 17, 17]