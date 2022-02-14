

N, Q = map(int, input().split())
queries = [list(map(int, input().split())) for _ in range(Q)]
front = [-1] * (N+1)
back = [-1] * (N+1)


for i in range(Q):
    query = queries[i]
    if query[0] == 1:
        back[query[1]] = query[2]
        front[query[2]] = query[1]
    elif query[0] == 2:
        back[query[1]] = -1
        front[query[2]] = -1
    else:
        num = query[1]
        ans = []
        while front[num] != -1:
            num = front[num]
        while num != -1:
            ans.append(num)
            num = back[num]
        print(len(ans), *ans)



