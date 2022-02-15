# N, W = map(int, input().split())
# wv = [list(map(int, input().split())) for _ in range(N)]  # [[3, 30], [4, 50],... ]
# DP = [[float('inf')]*(110000) for _ in range(N+1)]    # [[inf, inf, ...], [inf, inf, ...]]
# DP[0][0] = 0  # こうしないと(i,j)=(1,0)のときにうまくいかない

# # DP[i][j] i番目のお菓子を使って価値の総和がjになるときの重さの最小値
# # DP[i][j] = min(DP[i-1][j], DP[i-1][j-v[i]] + w[i])

# for i in range(1, N+1):
#     for j in range(110000):
#         DP[i][j] = DP[i-1][j]
#         if j-wv[i-1][1] >= 0:
#             DP[i][j] = min(DP[i][j], DP[i-1][j-wv[i-1][1]] + wv[i-1][0])

# ans = 0

# for k in range(110000):
#     if DP[N][k] <= W:
#         ans = max(ans, k)

# print(ans)





# DPの２次元リストのサイズが、N(商品数) * W(重さ) = 10**11 になるので、大きすぎる。
# DPの２次元リストのサイズが、N(商品数) * W(価値) = 10**7 になるので、許容範囲内。

# DP[i][j] : i番目までの商品を見て、総価値がjの時の、重さの最小値
# DP[i][j] = min(DP[i-1][j], DP[i-1][j-v(i)] + w(i))

# DP[0][0] = 0 の初期化の意味を解説する。
# 最小値をとるので、infで初期化するのは仕方ない。
# DP[i][j] = min(DP[i][j], DP[i-1][j-value[i]] + weight[i]) この式がポイントだ。
# j = value[i] になった時、DP[i-1][0] になるよね。
# この時に、0番目の値が0であってほしいよね、infではなく。
# 今のところここまでしかわからん。笑

N, W = map(int, input().split())
inf = float('inf')
weight = [inf]
value = [inf]
DP = [[inf]*((10**5)+1) for _ in range(N+1)]
DP[0][0] = 0

for _ in range(N):
    w, v = map(int, input().split())
    weight.append(w)
    value.append(v)

for i in range(1, N+1):
    for j in range((10**5)+1):
        DP[i][j] = DP[i-1][j]
        if j-value[i] >= 0:
            DP[i][j] = min(DP[i][j], DP[i-1][j-value[i]] + weight[i]) 

for i in range((10**5), -1, -1):
    if DP[N][i] <= W:
        print(i)
        break

# for row in DP:
#     print(row[:100])





