# N, Q =  map(int, input().split())
# A = list(map(int, input().split()))
# A.sort(reverse=True)
# ans = []

# for _ in range(Q):
#     x = int(input())
#     l = 0
#     r = len(A) - 1

#     if A[0] < x:
#         ans.append(0)
#         continue
#     elif A[0] == x:
#         ans.append(1)
#         continue
#     elif A[-1] >= x:
#         ans.append(len(A))
#         continue

#     while r - l > 1:
#         mid = (l+r) // 2
#         if A[mid] >= x:
#             l = mid
#         else:
#             r = mid
#     ans.append(r)

# for i in ans:
#     print(i)






# 2分探索  ng: ng < x  ok: x <= ok とする。

N, Q = map(int, input().split())
A = sorted(list(map(int, input().split())))
# print(A)

for _ in range(Q):
    l = 0
    r = N-1
    x = int(input())

    if x <= A[l]:
        print(N)
    elif A[N-1] < x:
        print(0)
    else:
        while r - l > 1:     # l - r = 1 になったら抜ける。ちょうどlとrが隣り合ったら終了。
            mid = (l+r) // 2
            if A[mid] >= x:
                r = mid
            else:
                l = mid
        print((N-1) - r + 1)       # 植木算


