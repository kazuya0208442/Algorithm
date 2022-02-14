from collections import deque

N, S, T = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]
que = deque()
count = 0

que.append([S, 0])   # [weight, day]

while que:
    weight, day = que.popleft()

    if weight > T:
        continue
    
    if day == N:
        count += 1
        continue

    a, b = AB[day]
    que.append([weight-a, day+1])
    que.append([weight+b, day+1])


print(count)