# import itertools

# N, X = map(int, input().split())
# jump_num = [list(map(int, input().split())) for _ in range(N)]
# max_sum = 0
# min_sum = 0

# for i, j in jump_num:
#     if i > j:
#         max_sum += i
#         min_sum += j
#     else:
#         max_sum += j
#         min_sum += i

# if not (min_sum <= X <= max_sum):
#     print('No')
#     exit()
# elif (min_sum == X) and (max_sum == X):
#     print('Yes')
#     exit()

# for product in set(itertools.product(*jump_num, repeat=1)):
#     sum = 0
#     for i in range(len(product)):
#         if sum < X:
#             sum += product[i]
#         else:
#             break
#         if (i == len(product) - 1) and (sum == X):
#             print('Yes')
#             exit()
        

# print('No')



# 0,1,2,3,4,5

import sys
sys.setrecursionlimit(10**6)

N, X = map(int, input().split())
jump_num = [list(map(int, input().split())) for _ in range(N)]
max_sum = 0
min_sum = 0

for i, j in jump_num:
    if i > j:
        max_sum += i
        min_sum += j
    else:
        max_sum += j
        min_sum += i

if not (min_sum <= X <= max_sum):
    print('No')
    exit()
elif (min_sum == X) or (max_sum == X):
    print('Yes')
    exit()
    


def dfs(index: int, sum: int):
    
    if (index == N) and (sum == X):
        print('Yes')
        exit()
    elif (index == N):
        return
    
    if (sum > X) or (sum + 100*(N-index) < X):
        return
    
    dfs(index+1, sum+jump_num[index][0])
    dfs(index+1, sum+jump_num[index][1])

dfs(0, 0)
print('No')


 



# from collections import deque

# N, X = map(int, input().split())
# jump_num = [list(map(int, input().split())) for _ in range(N)]
# max_sum = 0
# min_sum = 0
# que = deque()

# for i, j in jump_num:
#     if i > j:
#         max_sum += i
#         min_sum += j
#     else:
#         max_sum += j
#         min_sum += i

# if not (min_sum <= X <= max_sum):
#     print('No')
#     exit()
# elif (min_sum == X) or (max_sum == X):
#     print('Yes')
#     exit()

# que.append([0, 0])

# while que:
#     index, sum = que.popleft()

#     if (index == N) and (sum == X):
#         print('Yes')
#         exit()
#     elif index == N:
#         continue
#     elif sum + 100*(N-index) < X:
#         continue

#     for j in range(2):
#         if sum + jump_num[index][j] <= X:
#             que.append([index+1, sum + jump_num[index][j]])

# print('No')

