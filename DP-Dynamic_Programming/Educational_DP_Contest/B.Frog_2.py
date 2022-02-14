# N, K = map(int, input().split())
# h = list(map(int, input().split()))   # [h1, h2, h3, ...]
# inf = float('inf')
# DP = [inf] * N                     # [0, 0, 0, ...]
# DP[0] = 0

# for i in range(N):
#     for j in range(max(0, i-K), i):

#         DP[i] = min(DP[i], DP[j] + abs(h[i] - h[j]))

# # print(DP)
# print(DP[N-1])





# DP[i] = min(DP[i-K] + |h(i)-h(i-K)| : K ~ 1,2,...100)

N, K = map(int, input().split())
h = [float('inf')] + list(map(int, input().split()))
DP = [float('inf')] * (N+1)
DP[0] = 0
DP[1] = 0

for i in range(2, N+1):
    for k in range(1, min(i,K+1)):
        DP[i] = min(DP[i], DP[i-k] + abs(h[i]-h[i-k]))


print(DP[N])


