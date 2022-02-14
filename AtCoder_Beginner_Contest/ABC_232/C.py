# import itertools

# N, M = map(int, input().split())
# taka = [[] for _ in range(M+1)]
# aoki = [[] for _ in range(M+1)]
# N_list = [i+1 for i in range(N)]
# out = False

# for _ in range(M):
#     a, b = map(int, input().split())
#     taka[a].append(b)
#     taka[b].append(a)

# for _ in range(M):
#     c, d = map(int, input().split())
#     aoki[c].append(d)
#     aoki[d].append(c)

# if M == 0:
#     print('Yes')
#     exit()
    
# if N == 1:
#     print('Yes')
#     exit()

# for v in itertools.permutations(N_list):
#     for i in range(N-1):
#         for j in range(i+1, N):
#             if v[j] in aoki[v[i]]:
#                 if j+1 in taka[i+1]:
#                     continue
#                 else:
#                     out = True
#                     break
#         if out:
#             out = False
#             break
#     else:
#         print('Yes')
#         exit()


# print('No')        #WAだった





# itertoolsを使って解くぜ。これはやはりだめだ。各店ごとにいくつの点とつながっているのかを調べたけど１つエラーが出た。やっぱり、写像の式を使わないといけない。WA。

# import itertools
# from collections import defaultdict

# N, M = map(int, input().split())
# Taka_link_number = defaultdict(int)
# Ao_link_number = defaultdict(int)

# for _ in range(M):
#     A, B = map(int, input().split())
#     Taka_link_number[A] += 1
#     Taka_link_number[B] += 1

# for _ in range(M):
#     C, D = map(int, input().split())
#     Ao_link_number[C] += 1
#     Ao_link_number[D] += 1

# # print(Taka_link_number)
# # print(Ao_link_number)

# Taka_values_list = sorted(list(Taka_link_number.values()))
# Ao_values_list = sorted(list(Ao_link_number.values()))

# # print(Taka_values_list)

# if Taka_values_list == Ao_values_list:
#     print('Yes')
# elif not M:
#     print('Yes')
# else:
#     print('No')







# 写像Pをしっかり現わそう。

from collections import defaultdict
import itertools

N, M = map(int, input().split())
Taka_link_list = defaultdict(list)
Ao_link_list = defaultdict(list)

for _ in range(M):
    A, B = map(int, input().split())
    Taka_link_list[A].append(B)
    Taka_link_list[B].append(A)

for _ in range(M):
    C, D = map(int, input().split())
    Ao_link_list[C].append(D)
    Ao_link_list[D].append(C)

# print(Taka_link_list)
# print(Ao_link_list)

out = False
for P in itertools.permutations(range(1, N+1)):
    # P = (3,2,1,4)
    for i in range(1, N+1):
        for j in range(1, N+1):
            if (j in Taka_link_list[i]) != (P[j-1] in Ao_link_list[P[i-1]]):           # 複数条件は()で囲まないと間違えた結果を返すから気を付けて。
                out = True
                break
        if out:
            out = False
            break
    else:
        print('Yes')
        exit()

print('No')

                







                



