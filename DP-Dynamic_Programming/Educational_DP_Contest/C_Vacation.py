# N = int(input())
# h = [list(map(int, input().split())) for _ in range(N)]
# DP = [[0] * 3 for _ in range(N)]
# DP[0] = h[0]

# # DP[x][i] = max(DP[x-1][j](前日までの最大値) + h[x][i](今日の幸福度)) i!=jについての和

# for x in range(1, N):
#     for today_act in range(3):
#         for yesterday_act in range(3):
#             if today_act != yesterday_act:

#                 DP[x][today_act] = max(DP[x][today_act], DP[x-1][yesterday_act] + h[x][today_act])

# # print(DP)
# print(max(DP[N-1]))





# 変数は２つ。「何日目なのか」と「何をしたのか」
# DP[i][j] : i日目にjをしたとき、i日目までの幸福度の総和の最大値。
# 前日にやっていない活動が２つあり、そのうち大きいほうを選べばいい。
# DP[i][j] = max(DP[i-1][j 以外]) + act[j]

N = int(input())
activity = [0] + [list(map(int, input().split())) for _ in range(N)]
DP = [[0] * (3) for _ in range(N+1)]
DP[1] = activity[1]

for i in range(2, N+1):
    for j in range(3):
        DP[i][j] = max(DP[i-1][(j+1)%3], DP[i-1][(j+2)%3]) + activity[i][j]


print(max(DP[N]))



