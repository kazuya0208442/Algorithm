# [3,5]
# [5,7] ng
# [6,7] ok

# 0 1 2 3 4 5 6 7 8 9
# @ @ @
#     @ @ @
#       @ @ @
#            @ @ @


# 数直線上という条件から、小数や無理数などもあてはまるのでは？
# 座標も腕の長さも整数とは限らない。
# ok: [1,0.25] -> (left, right) = (0.75, 1.25) 
# ng: [1,0.25] -> [left, right] = [1-0.25+1, 1+0.25+1] = [1.75, 2.25]  


# N = int(input())
# left_right = []

# for _ in range(N):
#     X, L = map(int, input().split())
#     left, right = X-L+1, X+L-1
#     # left, right = X-L, X+L
#     # if left < 0:
#     #     left = 0
#     left_right.append([left, right])

# # print(left_right)
# left_right.sort(key=lambda x: x[1])
# # print(left_right)
# pointer = -float('inf')
# ans = 0

# for left, right in left_right:
#     if pointer < left:
#         pointer = right
#         ans += 1

# print(ans)






# X-L, X+L でやってみる
# 数直線上という条件から、小数や無理数などもあてはまるのでは？
# 座標も腕の長さも整数とは限らない。
# ok: [1,0.25] -> (left, right) = (0.75, 1.25) 
# ng: [1,0.25] -> [left, right] = [1-0.25+1, 1+0.25+1] = [1.75, 2.25] 
# これはACとれたよ

N = int(input())
left_right = []

for _ in range(N):
    X, L = map(int, input().split())
    # left, right = X-L+1, X+L-1
    left, right = X-L, X+L
    # if left < 0:
    #     left = 0
    left_right.append([left, right])

# print(left_right)
left_right.sort(key=lambda x: x[1])
# print(left_right)
pointer = -float('inf')
ans = 0

for left, right in left_right:
    if pointer <= left:
        pointer = right
        ans += 1

print(ans)






