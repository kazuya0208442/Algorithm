# from abc import abstractproperty
# import itertools

# N, X = map(int, input().split())
# price_list = [int(input()) for _ in range(N)]

# sorted_p_list = sorted(price_list)

# B = []


# for i in range(N-1):
#     sum_min = sum(sorted_p_list[:N-i])
#     if sum_min > X:
#         continue
#     else:
#         num = N-i
#         combinations = list(itertools.combinations(price_list, num))
#         A = [X] * len(combinations)

#         for i in range(len(combinations)):
#             for j in range(num):
#                 A[i] -= combinations[i][j]
#         break

# for i in range(len(A)):
#     if A[i] > 0:
#         B.append(A[i])

# print(min(B))






# DP[i][j] i個目までのお菓子を使って、j種類のお菓子を買ったときの、合計金額の最小値
# DP[i][j] = min(DP[i-1][j], DP[i-1][j-1] + v[i]) 

# N, X = map(int, input().split())
# price = [int(input()) for _ in range(N)]
# inf = float('inf')
# DP = [[0] + [inf] * (N) for _ in range(N+1)]  # [[0, inf,...], [0, 150, inf, ...], [0, inf, inf, ...]]
# DP[1][1] = price[0]

# for i in range(1, N+1):
#     for j in range(1, N+1):
#         if i > 1:
#             DP[i][j] = min(DP[i-1][j], DP[i-1][j-1] + price[i-1])

# print(DP)
# num = 0

# for k in range(N+1):
#     if DP[N][k] <= X:
#         num = max(num, k)







# DP[i][j] i個目までのお菓子を使って、j種類のお菓子を買ったときの、合計金額の最大値(X円以下で)
# DP[i][j] = max(DP[i-1][j], DP[i-1][j-1] + v[i]) 

# N, X = map(int, input().split())
# price = [int(input()) for _ in range(N)]
# # inf = float('inf')
# DP = [[0] * (N+1) for _ in range(N+1)]  # [[0, inf,...], [0, 150, inf, ...], [0, inf, inf, ...]]
# DP[1][1] = price[0]

# for i in range(2, N+1):
#     for j in range(1, i+1):
#             DP[i][j] = DP[i-1][j]
#             if DP[i-1][j-1] + price[i-1] <= X:
#                 DP[i][j] = max(DP[i][j], DP[i-1][j-1] + price[i-1])

# # print(DP)
# sum_p = 0

# for k in range(N+1):
#     if DP[N][k] <= X:
#         sum_p = max(sum_p, DP[N][k])

# print(X - sum_p)


# 合計金額を最小にするか最大にするかしか求められてない。






# DP[i][j] i個目までのお菓子を使って、j種類のお菓子を買ったときの、合計金額の最小値
# DP[i][j] = min(DP[i-1][j], DP[i-1][j-1] + v[i]) 

N, X = map(int, input().split())
price = [int(input()) for _ in range(N)]
inf = float('inf')
DP = [[0] + [inf] * (N) for _ in range(N+1)]  # [[0, inf,...], [0, 150, inf, ...], [0, inf, inf, ...]]
DP[1][1] = price[0]

for i in range(1, N+1):
    for j in range(1, N+1):
        if i > 1:
            DP[i][j] = min(DP[i-1][j], DP[i-1][j-1] + price[i-1])

# print(DP)
num = 0

for k in range(N+1):
    if DP[N][k] <= X:
        num = max(num, k)


import itertools
sum_p = 0

for x in itertools.combinations(price, num):
    if sum(x) <= X:
        sum_p = max(sum_p, sum(x))

print(X - sum_p)


