# 昇順をスライドさせてできた数列の中で最小値を見つける。
# 4 5 1 2 3

# 入力のサイズが10**8以下だったら、O(N)の方法で行ける。
# nums = list(map(int, input().split()))

# for i in range(len(nums)-1):
#     if nums[i] < nums[i+1]:
#         continue
#     else:
#         print(nums[i+1])
#         break
# else:
#     print(nums[0])



# 入力のサイズが10**8以上だったら、O(log(N))の方法で行ける。

nums = list(map(int, input().split()))
left = 0
right = len(nums) - 1

if nums[0] < nums[-1]:
    print(nums[0])
    exit()

while right - left > 1:
    mid = (right + left) // 2
    if nums[left] < nums[mid]:
        left = mid
    else:
        right = mid

print(nums[right])











