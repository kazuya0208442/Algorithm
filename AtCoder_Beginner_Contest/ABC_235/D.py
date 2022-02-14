# from collections import deque

# a, N = map(int, input().split())
# que = deque()
# s = set()

# que.append([N,0])
# s.add(N)
# # print(que)

# while que:
#     now, cnt = que.popleft()

#     if now == 1:
#         print(cnt)
#         exit()

#     if now % a == 0 and now//a not in s:
#         que.append([now//a, cnt+1])
#         s.add(now//a)

#     if len(str(now)) >= 2 and now % 10 != 0:
#         list_now = list(str(now))
#         new_now = int(''.join(list_now[1:] + list(list_now[0])))
#         # new_now = int(''.join(new_now))

#         if new_now not in s:
#             que.append([new_now, cnt+1])
#             s.add(new_now)

# print(-1)






# # 迷路と同じBFS

# from collections import deque

# a, N = map(int, input().split())
# numbers = [0] * (10**6)
# que = deque()

# que.append(1)


# while que:
#     now = que.popleft()

#     if now == N:
#         print(numbers[now])
#         exit()
    
#     if a*now < 10**6 and not numbers[a*now]:
#         que.append(a*now)
#         numbers[a*now] = numbers[now] + 1
    
#     if now % 10 != 0 and len(str(now)) >= 2:
#         now = str(now)
#         now_swapped = now[-1] + now[:-1]
#         now_swapped = int(now_swapped)

#         if now_swapped < 10**6 and not numbers[now_swapped]:
#             now = int(now)
#             que.append(now_swapped)
#             numbers[now_swapped] = numbers[now] + 1

# # print(numbers)
# print(-1)






# 解答

from collections import deque
a, N = map(int, input().split())
M = 1
while M <= N:
  M *= 10
d = [-1] * M
Q = deque()
d[1] = 0
Q.append(1)
while len(Q):
  c = Q.popleft()
  dc = d[c]
  op1 = a * c
  if op1 < M and d[op1] == -1:
    d[op1] = dc + 1
    Q.append(op1)
  if c >= 10 and c % 10 != 0:
    s = str(c)
    op2 = int(s[-1] + s[:-1])
    if op2 < M and d[op2] == -1:
      d[op2] = dc + 1
      Q.append(op2)
print(d[N])