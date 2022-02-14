# from collections import defaultdict

# N, Q = map(int, input().split())
# a = list(map(int, input().split()))
# xk = [list(map(int, input().split())) for _ in range(Q)]
# d = defaultdict(list)

# for i in range(N):
#     d[a[i]].append(i)

# for j in range(Q):
#     x, k = xk[j]

#     if len(d[x]) >= k:
#         print(d[x][k-1]+1)
#     else:
#         print(-1)





# defaultdict を使わない方法


N, Q = map(int, input().split())
a = list(map(int, input().split()))
dict = {}

for i in range(N):
    dict[a[i]] = dict.get(a[i], [])
    dict[a[i]].append(i)

for j in range(Q):
    x, k = map(int, input().split())

    if x in dict.keys() and k <= len(dict[x]):
        print(dict[x][k-1]+1)
        # print(dict[x][k-1]+1 == 2)
    else:
        print(-1)

