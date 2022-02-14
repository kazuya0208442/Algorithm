# from itertools import product

# # カッコ列 S が整合しているかどうか
# def isvalid(S):
#     score = 0
#     for c in S:
#         if c == '(':
#             score += 1
#         else:
#             score -= 1

#         # 途中で 0 を下回るとダメ
#         if score < 0:
#             return False

#     # 最後に 0 なら True、そうでなければ False
#     return (score == 0)

# N = int(input())
# for S in product(['(', ')'], repeat=N):
#     if (isvalid(S)):
#         # リストを文字列に
#         print(*S, sep='')     # 模範解答だよ


