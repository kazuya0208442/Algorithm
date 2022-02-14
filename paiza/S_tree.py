from collections import deque

N = int(input())
abc = [list(map(int, input().split())) for _ in range(N-1)]
route = [[] for _ in range(N+1)]
que = deque()

for i in range(N-1):
    route[abc[i][0]].append(abc[i][1])
    route[abc[i][1]].append(abc[i][0])

# [num, numから見たすべての重み] give up