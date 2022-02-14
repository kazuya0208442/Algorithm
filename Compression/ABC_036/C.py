N = int(input())
nums = [int(input()) for _ in range(N)]

sorted_nums = sorted(list(set(nums)))
dict = {num: index for index, num in enumerate(sorted_nums)}

for num in nums:
    print(dict[num])




