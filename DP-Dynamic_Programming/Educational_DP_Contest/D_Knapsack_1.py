

N, W = map(int, input().split())
w_v = [list(map(int, input().split())) for _ in range(N)]
DP = [[0] * (W+1) for _ in range(N+1)]

# DP[i][j] i番目のお菓子で重さがj以下になる選び方での価値の最大値
# DP[i][j] = max(DP[i-1][j], DP[i-1][j-w[i]] + v[i])

for i in range(1, N+1):
    for j in range(W+1):
        DP[i][j] = DP[i-1][j]
        if j-w_v[i-1][0] >= 0:
            DP[i][j] = max(DP[i][j], DP[i-1][j-w_v[i-1][0]] + w_v[i-1][1])

# print(DP)
print(DP[N][W])



# N ,W = map(int, input().split())
# dp = [0]*(W+1)
 
# for _ in range(0, N):
#     weight, value = map(int, input().split())
#     for w in range(W, weight-1, -1):
#         if dp[w-weight] + value > dp[w]:
#             dp[w] = dp[w-weight] + value
 
# print(dp[W])