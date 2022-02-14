from collections import deque

N, K = map(int, input().split())
nums = [int(input()) for _ in range(N)]
que = deque()
ans = 0
product = 1


for n in nums:
    que.append(n)
    product *= n 

    while que and product > K:
        que.popleft()
        product //= n 
    
    ans = max(ans, len(que))

# 左端を決めて右にどれだけ行けるか、の距離は、左端を進めていくと、最大の右端よりも減ることはない。
# スタート位置のカーソルを一つずつ増やしていく

# N, K = 7 , 6
# A = [4, 3, 1, 1, 2, 10, 2]
# deque([4])                  # 4スタートだと１個が限界
# deque([3])                  # 3スタートだと１個が限界
# deque([3, 1])               
# deque([3, 1, 1])　　　　　　
# deque([3, 1, 1, 2])         # 3スタートだと4個が限界
# deque([])
# deque([2])