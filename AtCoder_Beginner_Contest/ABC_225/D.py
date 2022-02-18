# N, Q = map(int, input().split())
# queries = [list(map(int, input().split())) for _ in range(Q)]
# front = [-1] * (N+1)
# back = [-1] * (N+1)


# for i in range(Q):
#     query = queries[i]
#     if query[0] == 1:
#         back[query[1]] = query[2]
#         front[query[2]] = query[1]
#     elif query[0] == 2:
#         back[query[1]] = -1
#         front[query[2]] = -1
#     else:
#         num = query[1]
#         ans = []
#         while front[num] != -1:
#             num = front[num]
#         while num != -1:
#             ans.append(num)
#             num = back[num]
#         print(len(ans), *ans)





# 電車の前と後ろに何がつながっているのかを配列で持っておく。

N, Q = map(int, input().split())
front = [-1] * (N+1)
back = [-1] * (N+1)
ans = []

for _ in range(Q):
    category, *nums = map(int, input().split())
    if category == 1:
        back[nums[0]] = nums[1]
        front[nums[1]] = nums[0]

    elif category == 2:
        back[nums[0]] = -1
        front[nums[1]] = -1

    else:
        target = nums[0]
        while front[target] != -1:
            target = front[target]

        train = [target]
        length_train = 1

        while back[target] != -1:
            train.append(back[target])
            target = back[target]
            length_train += 1

        ans.append([length_train, *train])

for row in ans:
    print(*row)









