# N = int(input())
# h = list(map(int, input().split()))  # [h1, h2, h3, ...]
# DP = [0] * N                   # [0, 0, 0, 0, ...]
# DP[0] = 0

# # DP[x] = min(DP[x-1] + |h[x-1] - h[x]|, DP[x-2] + |h[x-2] - h[x]|)
# # x個目の足場についたときに支払うコストの最小値をDP[x]とする。
# # DP[0] = 0

# for i in range(1, N):
#     if i == 1:
#         DP[i] = DP[0] + abs(h[i] - h[0])
#     else:
#         DP[i] = min(DP[i-1] + abs(h[i] - h[i-1]), DP[i-2] + abs(h[i] - h[i-2]))

# # print(DP)
# print(DP[N-1])




# DP[i]: i番目にいる時のコストの総和の最小値
# DP[i] = min(DP[i-1] + |h(i)-h(i-1)|, DP[i-2] + |h(i)-h(i-2)|)
# hの０番目にinfの壁を作ることで、０スタートになるように調整。

N = int(input())
h = [float('inf')] + list(map(int, input().split()))
DP = [float('inf')] * (N+1)
DP[0] = 0
DP[1] = 0

for i in range(2, N+1):
    DP[i] = min(DP[i-1] + abs(h[i]-h[i-1]), DP[i-2] + abs(h[i]-h[i-2]))

print(DP[N])







