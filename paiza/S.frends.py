# グループに 0 N の時に注意
# グループ内にいる数字をsetで管理する。
# グループ外もsetでもっておく。
# 追加の時は、グループ内にその数字を入れて、グループ外から削除する。
# グループ内の数字をループしてfrendをとってきて、グループ外のfrendだけとってきて、有効度を更新する。
# [a, b]: num みたいなdictがいる。

from collections import defaultdict

N, M, Q = map(int, input().split())
frend = [[] for _ in range(N+1)]
f_deg = defaultdict(int)                # defaultdict(<class 'int'>, {(1, 2): 1, (1, 3): 3})
in_g = set()
out_g = set(i for i in range(1, N+1))
f_max = 0
ans_list = []


for _ in range(M):
    a, b, f = map(int, input().split())
    frend[a].append(b)
    frend[b].append(a)
    f_deg[(a, b)] = f

for _ in range(Q):
    sign, num = input().split()
    num = int(num)

    if len(in_g) == N:
        ans_list.append('0')
        continue

    if sign == "+":
        in_g.add(num)
        out_g.discard(num)
        for i in in_g:
            for j in frend[i]:
                if j in out_g:
                    if i > j:
                        i, j = j, i
                    f_max = max(f_max, f_deg[(i, j)])
        ans_list.append(f_max)
        f_max = 0

    elif sign == "-":
        in_g.discard(num)
        out_g.add(num)

        if len(in_g) == 0:
            ans_list.append('0')
            continue

        for i in in_g:
            for j in frend[i]:
                if j in out_g:
                    if i > j:
                        i, j = j, i
                    f_max = max(f_max, f_deg[(i, j)])
        
        ans_list.append(f_max)
        f_max = 0


for i in ans_list:
    print(i)
                    





