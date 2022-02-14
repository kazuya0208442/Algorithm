N = int(input())
X, Y = map(int, input().split())
DP = [[[0]*301 for _ in range(301)] for _ in range(N+1)]
AB = [list(map(int, input().split())) for _ in range(N)]

# DP[i][j][k]  i個目までの弁当を使って、たこ焼きがj個以上でたこ焼きがk個以上の時の弁当の個数の最小値。
# DP[i][j][k] = min(DP[i-1][j][k], DP[i-1][j-w[i][0]][k-w[i][1]] + 1)

for i in range(1, N+1):
    for j in range(301):
        for k in range(301):
            DP[i][j][k] = DP[i-1][j][k]
            if j >= AB[i-1][0] and k >= AB[i-1][1]:
                DP[i][j][k] = min(DP[i][j][k], DP[i-1][j-AB[i-1][0]][k-AB[i-1][1]] + 1)

print(DP[N][X][Y])
