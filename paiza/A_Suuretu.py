# def main():
#     N = int(input())
#     A, B = map(int, input().split())
#     num_list = set()

#     if A > B:
#         large, small = A, B
#     else:
#         large, small = B, A

#     for i in range(int(200000/small)+1):    # 全て３の時の全枚数
#         len_num = len(num_list)
#         for j in range(i+1):
#             num = large * i - (large - small) * j
#             if num <= N:
#                 num_list.add(num)
#         if len_num == len(num_list):
#             break

#     if N not in num_list:
#         num_list.add(N)
    
#     ans = N + 1 - len(num_list)

#     print(ans)

# main()





N = int(input())
A, B = map(int, input().split())

from collections import deque
que = deque([0, A, B])
check = [False] * (N+1)


while que:
    now = que.popleft()
    if check[now]:
        continue
    check[now] = True
    for i in (now+A, now+B):
        if i > N:
            i = N
            check[i] = True
        else:
            que.append(i)

print(check.count(False))
        

    

