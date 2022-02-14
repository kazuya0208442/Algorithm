# que を使った尺取り法、TLE１２秒とかになった（笑）答えはあってるけど遅い。
# lとrを使う正攻法でもう一回やってみて、無理なら、累積和と二分探索の方法で行こう。

# from collections import deque

# N, Q = map(int, input().split())
# nums = list(map(int, input().split()))
# queries = list(map(int, input().split()))
# que = deque()


# for i in range(Q):
#     limit = queries[i]
#     index = 0
#     sum = 0
#     ans = 0
#     for _ in range(N):
#         while index < N and sum + nums[index] <= limit:
#             que.append(nums[index])   
#             sum += nums[index] 
#             index += 1
#         ans += len(que)
#         if que:
#             left = que.popleft()
#             sum -= left
#         else:
#             index += 1
#     print(ans)
            





# l, r の正攻法で行く  どんなに頑張ってもTLE
# r == l になったら、r+=1するのを忘れずに

# def main():

#     N, Q = map(int, input().split())
#     nums = list(map(int, input().split()))
#     queries = list(map(int, input().split()))

#     for i in range(Q):
#         limit = queries[i]
#         sum = 0
#         r = 0
#         ans = 0
#         for l in range(N):
#             while r < N and sum + nums[r] <= limit:
#                 sum += nums[r]
#                 r += 1
#             ans += r - l
#             if r == l:
#                 r += 1
#             else:
#                 sum -= nums[l]
#         print(ans)
        

# main()








# 累積和+二分探索で攻めるぜ。

N, Q = map(int, input().split())
nums = list(map(int, input().split()))
queries = list(map(int, input().split()))
accumulation = [0]

for i in range(N):
    accumulation.append(accumulation[i]+nums[i])

for i in range(Q):
    limit = queries[i]
    ans = 0
    for j in range(N):       # [l,r) -> S(r) - S(l)  ex) [1,3) -> S(3) - S(1) = 6-1=5
        if nums[j] > limit:    # 全てngの時を排除
            continue
        if accumulation[N] - accumulation[j] <= limit:    # 全てokの時を排除
            ans += N - j
            continue
        left = j
        right = N

        while right - left > 1:
            mid = (right+left) // 2
            if accumulation[mid] - accumulation[j] <= limit:
                left = mid
            else:
                right = mid
        
        ans += left - j          # [j,left)の累積和まではokなのです。個数はleft-j
    print(ans)







