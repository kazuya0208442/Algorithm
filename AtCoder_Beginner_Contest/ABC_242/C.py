# DP[i][j] : i番目の数字がjの時の場合の数
# DP[i][j] = DP[i-1][j-1] + DP[i-1][j] + DP[i-1][j+1]

N = int(input())
DP = [[0] * (10) for _ in range(N+1)]
mod = 998244353
ans = 0

for k in range(1, 10):
    DP[1][k] += 1

for i in range(2, N+1):
    for j in range(1, 10):
        DP[i][j] += DP[i-1][j]
        # DP[i][j] %= mod
        if j-1 >= 1:
            DP[i][j] += DP[i-1][j-1]
        if j+1 <= 9:
            DP[i][j] += DP[i-1][j+1]
        DP[i][j] %= mod


for v in DP[N]:
    ans += v
    ans %= mod

print(ans)









