# N = 2**20
# Q = int(input())
# tx = [list(map(int, input().split())) for _ in range(Q)]
# A = [-1 for _ in range(N)]

# for i in range(Q):
#     if tx[i][0] == 1:
#         h = tx[i][1]
#         while A[h % N] != -1:
#             h += 1
#         A[h % N] = tx[i][1]
#     else:
#         print(A[tx[i][1] % N])





# xの値がN-1の時に余りはN-1になって、x=Nの時に余りは0になる。　x=hに1を足してNで割った余りは、xがNの倍数の時に余り0になって、それまでは、余りも１ずつ増える。

# n = 1 << 20   # (2**20 = 1048576)  0 <= x <= 10**18 = 1000000000000000000
# p = [-1] * (n+1)
# A = [-1] * n

# def root(x):
#     if p[x] < 0:
#         return x
#     p[x] = root(p[x])
#     return p[x]

# def merge(x, y):
#     x = root(x)
#     y = root(y)
#     if x == y:
#         return
#     if x < y:
#         x, y = y, x
#     p[x] += p[y]
#     p[y] = x

# q = int(input())

# for _ in range(q):
#     t, x = map(int, input().split())
#     if t == 1:
#         h = x % n
#         target = root(h)
#         if target == n:
#             target = root(0)
#         A[target] = x
#         merge(target, target+1)
    
#     if t == 2:
#         print(A[x%n])


# print(p[:10])
# print(A[:10])





# import sys
# sys.setrecursionlimit(10**6)

# n = 1 << 20   # (2**20 = 1048576)  0 <= x <= 10**18 = 1000000000000000000
# p = [-1] * (n+1)
# A = [-1] * n

# def root(x):
#     if p[x] == -1:
#         return x
#     p[x] = root(p[x])
#     return p[x]

# def merge(x, y):
#     x = root(x)
#     y = root(y)
#     if x == y:
#         return
#     p[x] = y


# q = int(input())

# for _ in range(q):
#     t, x = map(int, input().split())
#     if t == 1:
#         h = x % n
#         target = root(h)
#         if target == n:
#             target = root(0)
#         A[target] = x
#         merge(target, target+1)
    
#     if t == 2:
#         print(A[x%n])


# print(p[:10])
# print(A[:10])




# import sys
# sys.setrecursionlimit(10**6)


# n = 1 << 20
# A = [-1] * n
# p = [-1] * n

# def root(x):
#     if p[x] == -1:
#         return x
#     p[x] = root(p[x])
#     return p[x]

# def merge(x, y):
#     x = root(x)
#     y = root(y)
#     if x == y:
#         return
#     p[x] = y            # merge(target, 0) でp[target] = root(0) にできるから、この場合だけ、大、小の順番で引数を入れる。


# q = int(input())

# for _ in range(q):
#     t, x = map(int, input().split())
#     num = x % n

#     if t == 2:
#         print(A[num])

#     elif t == 1:
#         target = root(num)
#         A[target] = x

#         if target == n-1:
#             merge(target, 0)
#             continue
        
#         merge(target, target+1)


    



# Q 回のforループを回す。
# 同じところに連打されると、１動かす操作を何回するのか。
# 初めは0回、次は1回とと増えていき、0+1+2+3+4+5+6+...Q
# 初項a, 末項l, 項数nのとき、Sn = n(a+l)/2
# つまり、命令の実行回数は、(Q+1)(0+Q) /2 = Q(Q+1)/2 = O(Q^2)

# mergeっぽいことを、親を書き換えるところでしている。
# 次に現れるー１以外の数字がある場所を親に設定するという狙い。


import sys
sys.setrecursionlimit(10**6)

N = 2**20
Q = int(input())
parents = [-1] * N
nums = [-1] * N

def root(x: int) -> int:
    if parents[x] == -1:
        return x
    parents[x] = root(parents[x])
    return parents[x]

for _ in range(Q):
    t, x = map(int, input().split())
    if t == 1:
        target = root(x % N)
        nums[target] = x
        if target == N-1:                  # targetに書き込んだ後に、targetの親を一個隣の親にする。N-1の時は0の親にする。1足してNで割ったら0だから。
            parents[target] = root(0)
        else:
            parents[target] = root(target+1)
    else:
        print(nums[x % N])


