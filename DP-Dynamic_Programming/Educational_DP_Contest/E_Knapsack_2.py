

N, W = map(int, input().split())
wv = [list(map(int, input().split())) for _ in range(N)]  # [[3, 30], [4, 50],... ]
DP = [[float('inf')]*(110000) for _ in range(N+1)]    # [[inf, inf, ...], [inf, inf, ...]]
DP[0][0] = 0  # こうしないと(i,j)=(1,0)のときにうまくいかない

# DP[i][j] i番目のお菓子を使って価値の総和がjになるときの重さの最小値
# DP[i][j] = min(DP[i-1][j], DP[i-1][j-v[i]] + w[i])

for i in range(1, N+1):
    for j in range(110000):
        DP[i][j] = DP[i-1][j]
        if j-wv[i-1][1] >= 0:
            DP[i][j] = min(DP[i][j], DP[i-1][j-wv[i-1][1]] + wv[i-1][0])

ans = 0

for k in range(110000):
    if DP[N][k] <= W:
        ans = max(ans, k)

print(ans)