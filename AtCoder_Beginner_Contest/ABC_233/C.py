# from collections import deque

# N, X = map(int, input().split())
# La = [list(map(int, input().split())) for _ in range(N)]
# que = deque()
# start = 0
# ans = 0

# for v in La[0][1:]:
#     que.append([v, start])



# while que:
#     now = que.popleft()
#     now_v = now[0]
#     now_i = now[1]

#     if now_i == N-1:
#         continue

#     for next_v in La[now_i+1][1:]:
#         if now_v * next_v == X and now_i == N-2:
#             ans += 1
#         elif now_v * next_v <= X:
#             que.append([now_v * next_v, now_i+1])

# print(ans)






# 再帰関数で解いてみる

# import sys
# sys.setrecursionlimit(10**6)

# N, X = map(int, input().split())
# bags = []
# balls = []
# ans = 0

# for _ in range(N):
#     temp = list(map(int, input().split()))
#     bag, ball = temp[0], temp[1:]
#     bags.append(bag)
#     balls.append(ball)

# def dfs(bag_index=0, product=1) -> None:

#     if bag_index == N and product == X:
#         global ans
#         ans += 1
#         return
#     elif bag_index == N:
#         return
    
#     for v in balls[bag_index]:
#         if product * v <= X:
#             dfs(bag_index+1, product * v)

# dfs()
# print(ans)






# itertools を使う！！

import itertools

N, X = map(int, input().split())
balls_count = []
ball_number = []
ans = 0


for _ in range(N):
    temp = list(map(int, input().split()))
    balls_count.append(temp[0])
    ball_number.append(temp[1:])

for product_list in itertools.product(*ball_number):
    # product_list = list(product_list)

    temp = 1

    for v in product_list:
        if temp*v > X:
            break
        temp *= v
    
    else:
        if temp == X:
            ans += 1

print(ans)



