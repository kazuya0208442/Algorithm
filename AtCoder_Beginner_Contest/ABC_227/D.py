# n, k = map(int, input().split())
# a = list(map(int, input().split()))

# def check(y):
#     ret = 0
#     for x in a:
#         ret += min(x, y)
#     return  ret >= y * k #条件をここに書く
 
# left = 0
# right = 10 ** 18 // k

# while left + 1 < right:
#     mid = (left + right) // 2
#     if check(mid):
#         left = mid
#     else:
#         right = mid

# #答えは最大値の時"left"最小値の時"right"。
# print(left)                                    # 模範解答  https://zenn.dev/fjnkt98/articles/5bef9f4cf2af60




N, K = map(int, input().split())
A = list(map(int, input().split()))
ok = 0
ng = 10 ** 18

def check(x):
    participants = 0
    for i in range(N):
        participants += min(A[i], x)
    if participants >= K * x:
        return True
    else:
        return False

while ng-ok > 1:
    mid = (ok + ng) // 2
    if check(mid):
        ok = mid
    else:
        ng = mid

print(ok)








# 作ることのできるプロジェクトの数をXとする。
# 一つのプロジェクトを構成する人数はK人とする。
# 合計人数は K*X 人になる。

# N = 3
# K = 3
# A1, A2, A3 = 2, 3, 4

# X = 2個のプロジェクトが作れると仮定すると、１つのプロジェクトの人数は３人なので、
#        1個目    2個目  (プロジェクト数X)
# 1人目    A1      A1
# 2人目    A2      A2
# 3人目    A3      A3
# (K人)
# 2個のプロジェクトは作れることが分かった。

# X = 3個のプロジェクトが作れると仮定すると、１つのプロジェクトの人数は３人なので、
#        1個目    2個目    3個目(プロジェクト数X)
# 1人目    A1      A1       A2
# 2人目    A2      A2       A3
# 3人目    A3      A3       ??
# (K人)
# 3個のプロジェクトは作れないことが分かった。A3からは3人が限度だから。
# A1: 2人, A2: 3人, A3: 3人, 合計で8人出せるが、3人グループを3つ作るには9人必要。

# つまり、各部署で選出できる人数はmin(プロジェクト数, 部署の人数)
# よって、Σ(1~N)min(プロジェクト数, 部署の人数) >= K*X なら、X個のプロジェクトが作れる。

# 最大人数の見積りが甘かった。
# (部署の人数) * (グループの人数) = (10**12) * (2*10**5) = 10**17 人
# K=1 の時、10**17個のプロジェクトが作れる



N, K = map(int, input().split())
nums = list(map(int, input().split()))
ok = 0
ng = 10**18             # ここの見極めが甘かった。

while ng-ok > 1:
    mid = (ng+ok)//2
    people = 0
    for num in nums:
        people += min(num, mid)
    if people >= K*mid:
        ok = mid
    else:
        ng = mid

print(ok)








