# mod = 998244353

# n = int(input())
# m = 3005

# A = list(map(int, input().split()))
# B = list(map(int, input().split()))

# dp = [[0]*m for _ in range(n)]

# for j in range(A[0], B[0]+1):
#     dp[0][j] += 1

# for i in range(n):
#     for j in range(A[i],B[i]+1):
#         if i > 0:
#             dp[i][j] = dp[i-1][j]
#     for j in range(m-1):
#         dp[i][j+1] += dp[i][j]
#         dp[i][j+1] %= mod

# print(dp[n-1][B[n-1]])



# i=0    co = 0        j = co = [0,...]
# i=1  1 <= c1 <= 2    j = c1 = [1, 2]
# i=2  1 <= c2 <= 4    j = c2 = [1, 2, 3, 4]
# i=2  1 <= c2 <= 5    j = c2 = [3, 4, 5]

# DP[i][j] = DP[i][j-1] + DP[i-1][j]
# DP = [[0,...], [0, 1, 2, 2, 2, 2, ...], [0, 1, 1+2, (1+2)+2, (1+2+2)+2, (1+2+2)+2,...], [0, 0, 0, 0+5, 5+7, 12+7, 12+7, ... ]]

N = int(input())
a = list(map(int, input().split()))     # a = [1, 1]
b = list(map(int, input().split()))     # b = [2, 3]
DP = [[0] * 3001 for _ in range(N+1)]
mod = 998244353


for i in range(1, N+1):
    for j in range(a[i-1], b[i-1]+1):
        if i == 1:
            DP[i][j] += j - a[i-1] + 1
            continue
        
        DP[i][j] = DP[i-1][j] % mod
        if j >= 0:
            DP[i][j] += DP[i][j-1]
            DP[i][j] %= mod
    for k in range(b[i-1]+1, 3001):
        DP[i][k] = DP[i][k-1]



print(DP[N][b[N-1]])
# print(DP[1][:100])
# print(DP[2][:100])
# print(DP[3][:100])






